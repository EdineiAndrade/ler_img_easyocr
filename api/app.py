from flask import Flask, request, jsonify
import easyocr
import os
import uuid

app = Flask(__name__)

# Inicializar o EasyOCR
reader = easyocr.Reader(['pt'])

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
    filepath = os.path.join('/tmp', filename)
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

# Rota padrão para verificar se o servidor está funcionando
@app.route('/')
def index():
    return 'Servidor Flask está funcionando!'

if __name__ == '__main__':
    app.run(debug=True)