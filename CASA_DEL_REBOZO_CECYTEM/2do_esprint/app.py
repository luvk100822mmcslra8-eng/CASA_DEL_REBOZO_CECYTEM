import sqlite3
from flask import Flask, render_template, request

app = Flask(_name_)
BASE_DATOS = "tienda.db"
CATEGORIAS = ["Rebozos", "Ropa", "Artesanías"]


def conectar():
    con = sqlite3.connect(BASE_DATOS)
    con.row_factory = sqlite3.Row
    return con


def crear_tabla():
    with conectar() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL,
                categoria TEXT NOT NULL
            )
        """)


def validar(nombre, precio, cantidad, categoria):
    """Devuelve (errores, precio_numero, cantidad_numero)."""
    errores = {}

    if len(nombre) < 3:
        errores["nombre"] = "Escribe el nombre del producto (mínimo 3 letras)."

    try:
        precio_n = float(precio)
        if precio_n <= 0:
            errores["precio"] = "El precio debe ser mayor a 0."
    except ValueError:
        precio_n = None
        errores["precio"] = "Escribe un precio válido, por ejemplo: 350."

    try:
        cantidad_n = int(cantidad)
        if cantidad_n < 0:
            errores["cantidad"] = "La cantidad no puede ser negativa."
    except ValueError:
        cantidad_n = None
        errores["cantidad"] = "Escribe una cantidad entera, por ejemplo: 10."

    if categoria not in CATEGORIAS:
        errores["categoria"] = "Selecciona una categoría."

    return errores, precio_n, cantidad_n


@app.route("/", methods=["GET", "POST"])
def productos():
    mensaje = ""
    tipo = ""
    errores = {}
    datos = {"nombre": "", "precio": "", "cantidad": "", "categoria": ""}

    if request.method == "POST":
        datos = {
            "nombre": request.form.get("nombre", "").strip(),
            "precio": request.form.get("precio", "").strip(),
            "cantidad": request.form.get("cantidad", "").strip(),
            "categoria": request.form.get("categoria", ""),
        }
        errores, precio_n, cantidad_n = validar(**datos)

        if errores:
            mensaje = "Revisa los campos marcados e inténtalo de nuevo."
            tipo = "error"
        else:
            with conectar() as con:
                con.execute(
                    "INSERT INTO productos (nombre, precio, cantidad, categoria) "
                    "VALUES (?, ?, ?, ?)",
                    (datos["nombre"], precio_n, cantidad_n, datos["categoria"]),
                )
            mensaje = "Producto registrado correctamente."
            tipo = "ok"
            datos = {"nombre": "", "precio": "", "cantidad": "", "categoria": ""}

    with conectar() as con:
        lista = con.execute("SELECT * FROM productos ORDER BY id DESC").fetchall()

    return render_template("productos.html", lista=lista, categorias=CATEGORIAS,
                           mensaje=mensaje, tipo=tipo, errores=errores, datos=datos)


if __name__ == "__main__":
    crear_tabla()
    app.run(debug=True)