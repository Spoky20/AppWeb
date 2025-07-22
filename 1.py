from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Ruta de prueba sin plantillas
@app.route('/prueba')
def prueba():
    return "<h1 style='color:green;font-size:30px;'>ESTE TEXTO VERDE DEBE SER VISIBLE</h1>"

# Versión ultra-simplificada de tu aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
    html_base = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generador LaTeX</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            .preview { background: #f0f0f0; padding: 15px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1 style="color:blue;">Generador LaTeX</h1>
        
        %ERROR%
        
        <form method="POST" enctype="multipart/form-data">
            <h3>Subir Excel:</h3>
            <input type="file" name="excel_file" accept=".xlsx,.xls">
            
            <h3>Tipo de ecuación:</h3>
            <select name="equation_type">
                <option value="Energía">Energía</option>
                <option value="Ley de Hooke">Ley de Hooke</option>
            </select>
            
            <button type="submit" style="margin-top:15px;padding:8px 15px;">
                Generar
            </button>
        </form>
        
        %PREVIEW%
        %LATEX%
    </body>
    </html>
    """
    
    if request.method == 'POST':
        try:
            # Procesamiento simulado
            preview = "<div class='preview'><h4>Datos de ejemplo:</h4><p>Tabla simulada</p></div>"
            latex = "<div class='preview'><h4>LaTeX:</h4><code>E = mc^2</code></div>"
            
            return render_template_string(
                html_base
                .replace("%ERROR%", "")
                .replace("%PREVIEW%", preview)
                .replace("%LATEX%", latex)
            )
        except Exception as e:
            return render_template_string(
                html_base.replace("%ERROR%", f"<div style='color:red;'>{str(e)}</div>")
            )
    
    return render_template_string(html_base.replace("%ERROR%", "").replace("%PREVIEW%", "").replace("%LATEX%", ""))

if __name__ == '__main__':
    app.run(debug=True, port=5000)