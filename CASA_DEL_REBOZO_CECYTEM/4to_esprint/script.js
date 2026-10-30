// Productos de ejemplo de Casa del Rebozo
const productos = [
    {
        nombre: "Rebozo mazahua",
        categoria: "Ropa",
        precio: 450,
        cantidad: 8
    },
    {
        nombre: "Blusa bordada",
        categoria: "Ropa",
        precio: 380,
        cantidad: 5
    },
    {
        nombre: "Falda tradicional",
        categoria: "Ropa",
        precio: 520,
        cantidad: 3
    },
    {
        nombre: "Bolsa artesanal",
        categoria: "Artesanía",
        precio: 250,
        cantidad: 6
    },
    {
        nombre: "Muñeca mazahua",
        categoria: "Artesanía",
        precio: 180,
        cantidad: 0
    }
];

// Mostrar los productos en la tabla
function mostrarInventario() {

    const tabla = document.getElementById("tabla-inventario");

    tabla.innerHTML = "";

    productos.forEach(producto => {

        const fila = document.createElement("tr");

        const estado = producto.cantidad > 0
            ? "Disponible"
            : "Sin existencias";

        fila.innerHTML = `
            <td>${producto.nombre}</td>
            <td>${producto.categoria}</td>
            <td>$${producto.precio.toFixed(2)}</td>
            <td>${producto.cantidad}</td>
            <td>${estado}</td>
        `;

        tabla.appendChild(fila);
    });
}

// Calcular el resumen del inventario
function calcularResumen() {

    const totalProductos = productos.length;

    const totalUnidades = productos.reduce(
        (suma, producto) => suma + producto.cantidad, 0
    );

    const sinExistencias = productos.filter(
        producto => producto.cantidad === 0
    ).length;

    document.getElementById("total-productos").textContent =
        totalProductos;

    document.getElementById("total-unidades").textContent =
        totalUnidades;

    document.getElementById("sin-existencias").textContent =
        sinExistencias;
}

// Descargar respaldo de información
function descargarRespaldo() {

    const respaldo = {
        tienda: "Casa del Rebozo",
        descripcion: "Respaldo del inventario de productos mazahuas",
        fecha: new Date().toLocaleString("es-MX"),
        productos: productos
    };

    const contenido = JSON.stringify(respaldo, null, 2);

    const archivo = new Blob(
        [contenido],
        { type: "application/json" }
    );

    const url = URL.createObjectURL(archivo);

    const enlace = document.createElement("a");

    enlace.href = url;

    enlace.download = "respaldo_casa_del_rebozo.json";

    enlace.click();

    URL.revokeObjectURL(url);

    document.getElementById("mensaje-respaldo").textContent =
        "El respaldo se descargó correctamente.";
}

// Botón para descargar el respaldo
document.getElementById("descargar-respaldo")
    .addEventListener("click", descargarRespaldo);

// Ejecutar las funciones al abrir la página
mostrarInventario();
calcularResumen();