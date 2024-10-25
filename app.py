from flask import Flask, render_template, url_for,jsonify,redirect,request
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/formulario')
def ingresarDatos():
    return render_template('formularioEcografia.html')

@app.route('/formularioH')
def ingresarDatosH():
    return render_template('formularioHistoria.html')

@app.route('/home')
def inicio():
    return render_template('home.html')

@app.route('/generar_pdf', methods=['POST'])
def generar_pdf():
    try:
        subdirectorio = "informesPDF/"
        data = request.form
        # Construye el nombre del archivo
        nombre_archivo = f"{subdirectorio}informe_{data['cedula']}_{data['apellido']}_{data['fecha']}.pdf"
        pdfkit.from_string(render_template('informe.html', **data), nombre_archivo, 
                        options={"page-size": "Letter", "encoding": "UTF-8"})
        return redirect(url_for('informe'))
        #return jsonify({"message": "PDF generado exitosamente"})
    except Exception as e:
        app.logger.error(f"Error al generar PDF: {e}")
        return redirect(url_for('errorPDF'))
        #return jsonify({"error": "Error al generar PDF"}), 500

@app.route('/generarH_pdf', methods=['POST'])
def generarH_pdf():
    try:
        subdirectorio = "informesPDF/"
        data = request.form
        # Construye el nombre del archivo
        nombre_archivo = f"{subdirectorio}Hinforme_{data['cedula']}_{data['apellido']}_{data['fecha']}.pdf"
        pdfkit.from_string(render_template('informeH.html', **data), nombre_archivo, 
                        options={"page-size": "Letter", "encoding": "UTF-8"})
        return redirect(url_for('informeH'))
        #return jsonify({"message": "PDF generado exitosamente"})
    except Exception as e:
        app.logger.error(f"Error al generar PDF: {e}")
        return redirect(url_for('errorPDF'))
        #return jsonify({"error": "Error al generar PDF"}), 500

@app.route('/informe')
def informe():
    return render_template('informe.html')

@app.route('/informeH')
def informeH():
    return render_template('informeH.html')

@app.route('/errorPDF')
def errorPDF():
    return render_template('errorPDF.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0",port=80)