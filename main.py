from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')


@app.route('/phone_scammers')
def phone_scamers():
    return render_template('phone_scammers.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/add_phone', methods=['POST', 'GET'])
def add_phone():
    if request.method == 'GET':
        return render_template('add_phone.html')
    elif request.method == 'POST':
        print(request.form['mobile'])
        print(request.form['message'])
        print(request.form['datetime-local'])
        print(request.form['regions'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
