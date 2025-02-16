from flask import Flask, request, jsonify, render_template
import os
import uuid
import tempfile
import easyocr

app = Flask(__name__)

# Inicializar o EasyOCR
reader = easyocr.Reader(['pt'])

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o HTML

# Rota para processar o upload da imagem
@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo inválido'}), 400

    # Salvar o arquivo temporariamente
    filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
    filepath = os.path.join(tempfile.gettempdir(), filename)
    file.save(filepath)

    # Realizar o OCR
    try:
        results = reader.readtext(filepath)
        text = ' '.join([result[1] for result in results])  # Unir todos os textos detectados
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Remover o arquivo temporário
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
