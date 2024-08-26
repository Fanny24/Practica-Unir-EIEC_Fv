from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response

app = Flask(__name__)

# Lista para almacenar los contactos
contactos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        celular = request.form['celular']

        # Agregar los datos a la lista de contactos
        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'celular': celular
        })

        # Redirigir para evitar el reenvío del formulario
        return redirect(url_for('index'))

    # Renderizar la página con los contactos actuales
    return render_template('index.html', contactos=contactos)

@app.route('/eliminar', methods=['POST'])
def eliminar():
    index = int(request.form['index'])
    if 0 <= index < len(contactos):
        del contactos[index]
    return jsonify({'status': 'success'})

@app.route('/exportar', methods=['GET'])
def exportar():
    # Crear el contenido del archivo
    contenido = "Nombre\tApellido\tCorreo Electrónico\tCelular\n"
    for contacto in contactos:
        contenido += f"{contacto['nombre']}\t{contacto['apellido']}\t{contacto['correo']}\t{contacto['celular']}\n"

    # Crear la respuesta con el archivo .txt
    response = make_response(contenido)
    response.headers["Content-Disposition"] = "attachment; filename=contactos.txt"
    response.headers["Content-Type"] = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)
