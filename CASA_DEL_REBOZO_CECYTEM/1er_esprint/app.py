# Datos de demostración (Sprint 1)
USUARIO_ADMIN = "admin"
CLAVE_ADMIN = "rebozo123"

PRODUCTOS = [
    {"nombre": "Rebozo mazahua tradicional",
     "descripcion": "Rebozo tejido a mano con diseños tradicionales.",
     "precio": 350},
    {"nombre": "Blusa bordada mazahua",
     "descripcion": "Blusa de manta con bordado artesanal.",
     "precio": 450},
    {"nombre": "Muñeca de trapo mazahua",
     "descripcion": "Muñeca artesanal con atuendo típico.",
     "precio": 200},
]


@app.route("/", methods=["GET", "POST"])
def inicio():
    mensaje = ""
    tipo = ""
    errores = {}

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        clave = request.form.get("clave", "")

        # Validación de campos obligatorios
        if usuario == "":
            errores["usuario"] = "Escribe tu usuario."
        if clave == "":
            errores["clave"] = "Escribe tu contraseña."

        # Validación de usuario y contraseña
        if not errores:
            if usuario == USUARIO_ADMIN and clave == CLAVE_ADMIN:
                mensaje = "Acceso correcto. Bienvenido, administrador."
                tipo = "ok"
            else:
                mensaje = "Usuario o contraseña incorrectos. Inténtalo de nuevo."
                tipo = "error"

    return render_template("index.html", productos=PRODUCTOS,
                           mensaje=mensaje, tipo=tipo, errores=errores)


if __name__ == "__main__":
    app.run(debug=True)