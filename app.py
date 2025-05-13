from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def contacts():
    # Возвращаем страницу "Контакты" на любой GET-запрос
    return render_template('contacts.html')

@app.route('/', methods=['POST'])
def handle_post():
    # Обработка POST-запроса (дополнительное задание)
    data = request.form.to_dict()
    print("Received POST data:", data)
    return "POST request received. Data printed to console.", 200

if __name__ == '__main__':
    app.run(debug=True)
