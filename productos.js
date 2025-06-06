// Este script obtiene los productos del backend y los muestra en la página

function cargarProductos() {
  let url = 'http://localhost:8080/productos';
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
      console.error('Error:', error);
    });
}

// Cargar productos al cargar la página
document.addEventListener('DOMContentLoaded', () => {
  cargarProductos();
});
