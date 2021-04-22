import datetime
import sqlite3

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
    con = sqlite3.connect("db/phone_scammers.db")
    cr = con.cursor()
    numbers = cr.execute("""SELECT NUMBER FROM phones
                WHERE NUMBER > 0""").fetchall()
    phones = cr.execute("""SELECT PHONE FROM phones
                WHERE NUMBER > 0""").fetchall()
    texts = cr.execute("""SELECT TEXT FROM phones
                WHERE NUMBER > 0""").fetchall()
    datetimes = cr.execute("""SELECT DATETIME FROM phones
                WHERE NUMBER > 0""").fetchall()
    regions = cr.execute("""SELECT REGION FROM phones
                WHERE NUMBER > 0""").fetchall()
    links = []
    for i in numbers:
        a = '/topic/ps/' + i
        links.append(a)
    return render_template('test.html', numbers=numbers, phones=phones, texts=texts, datetimes=datetimes,
                           regions=regions, links=links)


@app.route('/add_phone', methods=['POST', 'GET'])
def add_phone():
    if request.method == 'GET':
        return render_template('add_phone.html')
    elif request.method == 'POST':
        con = sqlite3.connect("db/phone_scammers.db")
        cr = con.cursor()
        numbers = cr.execute("""SELECT NUMBER FROM phones
                    WHERE NUMBER > 0""").fetchall()
        if numbers == []:
            number = 1
        else:
            number = max(numbers) + 1
        phone = request.form['mobile']
        text = request.form['message']
        data_time = request.form['datetime-local']
        data_time = data_time.replace('T', ' ')
        print(data_time)
        region = request.form['regions']
        cr.execute("""INSERT INTO phones(NUMBER,PHONE,TEXT,DATETIME,REGION) VALUES(?,?,?,?,?)""",
                   (number, phone, text, data_time, region))
        print(request.form['mobile'])
        print(request.form['message'])
        print(request.form['datetime-local'])
        print(request.form['regions'])
        return render_template('return.html')


@app.route('/topic/ps/<int:number>')
def topic_ps(number):
    return


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
