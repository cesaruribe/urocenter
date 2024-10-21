from flask import Flask, render_template, request, redirect,url_for,flash,session
import pdfkit

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/formulario')
def ingresarDatos():
    return render_template('formularioEcografia.html')

@app.route('/home')
def inicio():
    return render_template('home.html')

@app.route('/generar_pdf', methods=['POST'])
def generar_pdf():
    data = request.form
    cedula = data['cedula'] 
    fecha = data['fecha']
    # Construye el nombre del archivo
    nombre_archivo = f"informe_{cedula}_{fecha}.pdf"
    pdfkit.from_string(render_template('informe.html', **data), nombre_archivo)
    return redirect(url_for('informe'))

@app.route('/informe')
def informe():
    return render_template('informe.html')

if __name__ == '__main__':
    app.run(host='100.29.14.242', port=80)
    #app.run(debug=True)