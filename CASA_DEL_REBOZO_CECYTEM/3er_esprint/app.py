import re
import sqlite3
from functools import wraps
from flask import (Flask, render_template, request, redirect,
                   url_for, session, flash)

app = Flask(__name__)
app.secret_key = "casa-del-rebozo-clave-de-ejemplo"

BASE_DATOS = "tienda.db"
CATEGORIAS = ["Rebozos", "Ropa", "Artesanías"]

# Datos de demostración del administrador (Sprint 1)
USUARIO_ADMIN = "admin"
CLAVE_ADMIN = "rebozo123"


# ---------- Base de datos ----------
def conectar():
    con = sqlite3.connect(BASE_DATOS)
    con.row_factory = sqlite3.Row
    return con


def preparar_base():
    with conectar() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT DEFAULT '',
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL,
                categoria TEXT NOT NULL,
                imagen TEXT DEFAULT ''
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                telefono TEXT NOT NULL,
                direccion TEXT NOT NULL
            )
        """)
        total = con.execute("SELECT COUNT(*) AS n FROM productos").fetchone()["n"]
        if total == 0:
            demo = [
                ("Rebozo mazahua tradicional", "Rebozo tejido a mano con diseños tradicionales.", 350, 10, "Rebozos", "rebozo1.jpg"),
                ("Blusa bordada mazahua", "Blusa de manta con bordado artesanal.", 450, 8, "Ropa", "blusa1.jpg"),
                ("Muñeca de trapo mazahua", "Muñeca artesanal vestida con atuendo típico.", 200, 15, "Artesanías", "muneca1.jpg"),
            ]
            con.executemany(
                "INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria, imagen) "
                "VALUES (?, ?, ?, ?, ?, ?)", demo)


# ---------- Protección de páginas de administrador ----------
def solo_admin(vista):
    @wraps(vista)
    def envoltura(*args, **kwargs):
        if not session.get("admin"):
            flash("Inicia sesión como administrador para entrar.", "error")
            return redirect(url_for("login"))
        return vista(*args, **kwargs)
    return envoltura


# ---------- Sprint 3: catálogo (PB-03) ----------
@app.route("/")
def catalogo():
    categoria = request.args.get("categoria", "Todos")
    with conectar() as con:
        if categoria in CATEGORIAS:
            productos = con.execute(
                "SELECT * FROM productos WHERE categoria = ? ORDER BY nombre",
                (categoria,)).fetchall()
        else:
            categoria = "Todos"
            productos = con.execute("SELECT * FROM productos ORDER BY nombre").fetchall()
    return render_template("catalogo.html", productos=productos,
                           categorias=CATEGORIAS, actual=categoria)


# ---------- Sprint 1: inicio de sesión (PB-01) ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    errores = {}
    usuario = ""
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        clave = request.form.get("clave", "")

        if usuario == "":
            errores["usuario"] = "Escribe tu usuario."
        if clave == "":
            errores["clave"] = "Escribe tu contraseña."

        if not errores:
            if usuario == USUARIO_ADMIN and clave == CLAVE_ADMIN:
                session["admin"] = True
                flash("Acceso correcto. Bienvenido, administrador.", "ok")
                return redirect(url_for("productos"))
            flash("Usuario o contraseña incorrectos. Inténtalo de nuevo.", "error")

    return render_template("login.html", errores=errores, usuario=usuario)


@app.route("/logout")
def logout():
    session.pop("admin", None)
    flash("Sesión cerrada.", "ok")
    return redirect(url_for("catalogo"))


# ---------- Sprint 2: registro de productos (PB-02) ----------
def validar_producto(d):
    errores = {}
    precio = cantidad = None

    if len(d["nombre"]) < 3:
        errores["nombre"] = "Escribe el nombre del producto (mínimo 3 letras)."

    try:
        precio = float(d["precio"])
        if precio <= 0:
            errores["precio"] = "El precio debe ser mayor a 0."
    except ValueError:
        errores["precio"] = "Escribe un precio válido, por ejemplo: 350."

    try:
        cantidad = int(d["cantidad"])
        if cantidad < 0:
            errores["cantidad"] = "La cantidad no puede ser negativa."
    except ValueError:
        errores["cantidad"] = "Escribe una cantidad entera, por ejemplo: 10."

    if d["categoria"] not in CATEGORIAS:
        errores["categoria"] = "Selecciona una categoría."

    return errores, precio, cantidad


@app.route("/admin/productos", methods=["GET", "POST"])
@solo_admin
def productos():
    errores = {}
    datos = {"nombre": "", "descripcion": "", "precio": "",
             "cantidad": "", "categoria": "", "imagen": ""}

    if request.method == "POST":
        datos = {campo: request.form.get(campo, "").strip() for campo in datos}
        errores, precio, cantidad = validar_producto(datos)

        if errores:
            flash("Revisa los campos marcados e inténtalo de nuevo.", "error")
        else:
            with conectar() as con:
                con.execute(
                    "INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria, imagen) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (datos["nombre"], datos["descripcion"], precio, cantidad,
                     datos["categoria"], datos["imagen"]))
            flash("Producto registrado correctamente.", "ok")
            return redirect(url_for("productos"))

    with conectar() as con:
        lista = con.execute("SELECT * FROM productos ORDER BY id DESC").fetchall()
    return render_template("productos.html", lista=lista, categorias=CATEGORIAS,
                           errores=errores, datos=datos)


# ---------- Sprint 4: registro de clientes (PB-04) ----------
def validar_cliente(d):
    errores = {}
    if len(d["nombre"]) < 3:
        errores["nombre"] = "Escribe el nombre completo (mínimo 3 letras)."

    if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", d["correo"]):
        errores["correo"] = "Escribe un correo válido, por ejemplo: nombre@correo.com."
    else:
        with conectar() as con:
            existe = con.execute("SELECT 1 FROM clientes WHERE lower(correo) = lower(?)",
                                 (d["correo"],)).fetchone()
        if existe:
            errores["correo"] = "Este correo ya está registrado."

    if not re.match(r"^\d{10}$", d["telefono"]):
        errores["telefono"] = "El teléfono debe tener 10 números."

    if len(d["direccion"]) < 5:
        errores["direccion"] = "Escribe la dirección completa."
    return errores


@app.route("/admin/clientes", methods=["GET", "POST"])
@solo_admin
def clientes():
    errores = {}
    datos = {"nombre": "", "correo": "", "telefono": "", "direccion": ""}

    if request.method == "POST":
        datos = {campo: request.form.get(campo, "").strip() for campo in datos}
        errores = validar_cliente(datos)

        if errores:
            flash("Revisa los campos marcados e inténtalo de nuevo.", "error")
        else:
            with conectar() as con:
                con.execute(
                    "INSERT INTO clientes (nombre, correo, telefono, direccion) "
                    "VALUES (?, ?, ?, ?)",
                    (datos["nombre"], datos["correo"], datos["telefono"], datos["direccion"]))
            flash("Cliente registrado correctamente.", "ok")
            return redirect(url_for("clientes"))

    with conectar() as con:
        lista = con.execute("SELECT * FROM clientes ORDER BY id DESC").fetchall()
    return render_template("clientes.html", lista=lista, errores=errores, datos=datos)


if __name__ == "__main__":
    preparar_base()
    app.run(debug=True)