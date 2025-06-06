// Este script obtiene los productos del backend y los muestra en la página

function cargarCategorias() {
  fetch('http://localhost:8080/categorias')
    .then(response => response.json())
    .then(categorias => {
      const contenedor = document.getElementById('categorias-botones');
      contenedor.innerHTML = '';
      categorias.forEach(cat => {
        const btn = document.createElement('button');
        btn.className = 'btn-categoria';
        btn.textContent = cat;
        btn.onclick = () => {
          // Alternar selección visual
          document.querySelectorAll('.btn-categoria').forEach(b => b.classList.remove('activo'));
          btn.classList.add('activo');
          cargarProductos(cat);
        };
        contenedor.appendChild(btn);
      });
      // Botón para mostrar todos
      const btnTodos = document.createElement('button');
      btnTodos.className = 'btn-categoria';
      btnTodos.textContent = 'Todas';
      btnTodos.onclick = () => {
        document.querySelectorAll('.btn-categoria').forEach(b => b.classList.remove('activo'));
        btnTodos.classList.add('activo');
        cargarProductos();
      };
      contenedor.insertBefore(btnTodos, contenedor.firstChild);
      btnTodos.classList.add('activo');
    })
    .catch(error => {
      console.error('Error al cargar categorías:', error);
    });
}

function cargarProductos(categoria = "") {
  let url = 'http://localhost:8080/productos';
  if (categoria) {
    url += `?categoria=${encodeURIComponent(categoria)}`;
  }
  fetch(url)
    .then(response => response.json())
    .then(productos => {
      const contenedor = document.getElementById('productos');
      if (productos.length === 0) {
        contenedor.innerHTML = '<p>No hay productos disponibles.</p>';
        return;
      }
      contenedor.innerHTML = "";
      productos.forEach(producto => {
        const div = document.createElement('div');
        div.className = 'producto';
        div.innerHTML = `
          <img src="${producto.url}" alt="${producto.nombre}">
          <h2>${producto.nombre}</h2>
          <p class="precio">$${producto.precio}</p>
        `;
        contenedor.appendChild(div);
      });
    })
    .catch(error => {
      document.getElementById('productos').innerHTML = '<p>Error al cargar los productos.</p>';
      console.error('Error al cargar productos:', error);
    });
}

// Cargar categorías y productos al cargar la página
document.addEventListener('DOMContentLoaded', () => {
  // Crear contenedor de botones de categorías si no existe (ya lo añadimos en HTML)
  // const categoriasDiv = document.createElement('div');
  // categoriasDiv.id = 'categorias-botones';
  // categoriasDiv.className = 'categorias-botones';
  // document.querySelector('.filtro-categorias').appendChild(categoriasDiv);
  cargarCategorias();
  cargarProductos();
});
