// Este script obtiene los productos del backend y los muestra en la página

function cargarProductos() {
  let url = 'http://localhost:8000/productos';
  console.log(`Fetching products from: ${url}`); // Log the URL being fetched
  fetch(url)
    .then(response => {
      console.log('Received response:', response); // Log the response object
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(productos => {
      console.log('Received products data:', productos); // Log the received data
      const contenedor = document.getElementById('productos');
      if (!contenedor) {
          console.error('Products container element not found!'); // Log if container is missing
          return;
      }
      if (productos.length === 0) {
        contenedor.innerHTML = '<p>No hay productos disponibles.</p>';
        console.log('No products available.'); // Log if no products are found
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
      console.log(`Displayed ${productos.length} products.`); // Log the number of products displayed
    })
    .catch(error => {
      document.getElementById('productos').innerHTML = '<p>Error al cargar los productos.</p>';
      console.error('Error al cargar productos:', error); // Log any errors during fetch or processing
    });
}

// Cargar productos al cargar la página
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM fully loaded and parsed'); // Log when DOM is ready
  cargarProductos(); // Load all products by default
});
