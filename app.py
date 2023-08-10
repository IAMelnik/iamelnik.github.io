from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'Файл не выбран', 400

    file = request.files['file']
    if file.filename == '':
        return 'Файл не выбран', 400

    # Здесь вы можете выполнить дополнительные действия с загруженным файлом
    print('Загружен файл:', file.filename)

    return 'Файл успешно загружен'

if __name__ == '__main__':
    app.run(debug=True)
