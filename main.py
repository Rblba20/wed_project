import sqlite3

from flask import Flask, request, url_for, render_template
from phone_data import create
from sn_data import create_sn
from si_data import create_si

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')


@app.route('/phone_scammers')
def phone_scammers():
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
        a = '/topic/ps/' + str(i)[1:2]
        links.append(a)
    print(numbers, phones, texts, datetimes, regions, links)
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])[1:-2]
    for i in range(len(datetimes)):
        datetimes[i] = str(datetimes[i])[2:-3]
    for i in range(len(phones)):
        phones[i] = str(phones[i])[1:-2]
    for i in range(len(texts)):
        texts[i] = str(texts[i])[2:-3]
    for i in range(len(regions)):
        regions[i] = str(regions[i])[2:-3]
    return render_template('phone_scammers.html', numbers=numbers, phones=phones, texts=texts, datetimes=datetimes,
                           regions=regions, links=links)


@app.route('/add_phone', methods=['POST', 'GET'])
def add_phone():
    if request.method == 'GET':
        return render_template('add_phone.html')
    elif request.method == 'POST':
        phone = request.form['mobile']
        text = request.form['message']
        data_time = request.form['datetime-local']
        data_time = data_time.replace('T', ' ')
        phone = str(phone)
        text = str(text)
        data_time = str(data_time)
        region = request.form['regions']
        region = str(region)
        print(data_time, phone, text, region)
        a, b, c, d = data_time, phone, text, region
        fout = open("data.txt", "wt", encoding="utf8")
        str_ = a + '_&_' + b + '_&_' + c + '_&_' + d
        fout.write(str_)
        fout.close()
        create()
        return render_template('return.html')


@app.route('/topic/ps/<int:number>')
def topic_ps(number):
    con = sqlite3.connect("db/phone_scammers.db")
    cr = con.cursor()
    phones = cr.execute("""SELECT PHONE FROM phones
               WHERE NUMBER > 0""").fetchall()
    texts = cr.execute("""SELECT TEXT FROM phones
               WHERE NUMBER > 0""").fetchall()
    datetimes = cr.execute("""SELECT DATETIME FROM phones
               WHERE NUMBER > 0""").fetchall()
    regions = cr.execute("""SELECT REGION FROM phones
               WHERE NUMBER > 0""").fetchall()
    for i in range(len(datetimes)):
        datetimes[i] = str(datetimes[i])[2:-3]
    for i in range(len(phones)):
        phones[i] = str(phones[i])[1:-2]
    for i in range(len(texts)):
        texts[i] = str(texts[i])[2:-3].strip()
    for i in range(len(regions)):
        regions[i] = str(regions[i])[2:-3]
    number = int(number) - 1
    return render_template('topics_ps.html', number=number, phones=phones, texts=texts, datetimes=datetimes,
                           regions=regions)


@app.route('/scam_on_social_networks')
def scammers_on_social_networks():
    con = sqlite3.connect("db/scammers_on_social_networks.db")
    cr = con.cursor()
    numbers = cr.execute("""SELECT NUMBER FROM networks
                WHERE NUMBER > 0""").fetchall()
    links_n = cr.execute("""SELECT LINK FROM networks
                WHERE NUMBER > 0""").fetchall()
    texts = cr.execute("""SELECT TEXT FROM networks
                WHERE NUMBER > 0""").fetchall()
    dates = cr.execute("""SELECT DATA FROM networks
                WHERE NUMBER > 0""").fetchall()
    headings = cr.execute("""SELECT HEADING FROM networks
                WHERE NUMBER > 0""").fetchall()
    links = []
    for i in numbers:
        a = '/topic/sns/' + str(i)[1:2]
        links.append(a)
    print(numbers, links_n, texts, dates, links, headings)
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])[1:-2]
    for i in range(len(dates)):
        dates[i] = str(dates[i])[2:-3]
    for i in range(len(links_n)):
        links_n[i] = str(links_n[i])[2:-3]
    for i in range(len(texts)):
        texts[i] = str(texts[i])[2:-3]
    for i in range(len(headings)):
        headings[i] = str(headings[i])[2:-3]
    print(numbers, links_n, texts, dates, links, headings)
    return render_template('sn_scammers.html', numbers=numbers, headings=headings, texts=texts, dates=dates,
                           links_n=links_n, links=links)


@app.route('/add_sn', methods=['POST', 'GET'])
def add_sn():
    if request.method == 'GET':
        return render_template('add_sn.html')
    elif request.method == 'POST':
        heading = request.form['heading']
        text = request.form['message']
        date = request.form['date']
        link_ = request.form['link']
        print(date, heading, text, link_)
        fout = open("data.txt", "wt", encoding="utf8")
        str_ = heading + '_&_' + link_ + '_&_' + date + '_&_' + text
        fout.write(str_)
        fout.close()
        create_sn()
        return render_template('return.html')


@app.route('/topic/sns/<int:number>')
def topic_sn(number):
    con = sqlite3.connect("db/scammers_on_social_networks.db")
    cr = con.cursor()
    link_ = cr.execute("""SELECT LINK FROM networks
                WHERE NUMBER > 0""").fetchall()
    text = cr.execute("""SELECT TEXT FROM networks
                WHERE NUMBER > 0""").fetchall()
    date = cr.execute("""SELECT DATA FROM networks
                WHERE NUMBER > 0""").fetchall()
    for i in range(len(date)):
        date[i] = str(date[i])[2:-3]
    for i in range(len(link_)):
        link_[i] = str(link_[i])[2:-3]
    for i in range(len(text)):
        text[i] = str(text[i])[2:-3]
    number = int(number) - 1
    return render_template('topic_sn.html', number=number, link=link_, text=text, date=date, )


@app.route('/scam_in_the_internet')
def scam_in_the_internet():
    con = sqlite3.connect("db/scammers_in_the_internet.db")
    cr = con.cursor()
    numbers = cr.execute("""SELECT NUMBER FROM internet WHERE NUMBER > 0""").fetchall()
    links_i = cr.execute("""SELECT LINK FROM internet
                WHERE NUMBER > 0""").fetchall()
    texts = cr.execute("""SELECT TEXT FROM internet
                WHERE NUMBER > 0""").fetchall()
    headings = cr.execute("""SELECT HEADING FROM internet
                WHERE NUMBER > 0""").fetchall()
    links = []
    for i in numbers:
        a = '/topic/si/' + str(i)[1:2]
        links.append(a)
    print(numbers, links_i, texts, links, headings)
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])[1:-2]
    for i in range(len(links_i)):
        links_i[i] = str(links_i[i])[2:-3]
    for i in range(len(texts)):
        texts[i] = str(texts[i])[2:-3]
    for i in range(len(headings)):
        headings[i] = str(headings[i])[2:-3]
    print(numbers, links_i, texts, links, headings)
    return render_template('si_scammers.html', numbers=numbers, headings=headings, texts=texts,
                           links_i=links_i, links=links)


@app.route('/add_si', methods=['POST', 'GET'])
def add_si():
    if request.method == 'GET':
        return render_template('add_si.html')
    elif request.method == 'POST':
        heading = request.form['heading']
        text = request.form['message']
        link_ = request.form['link']
        print(heading, text, link_)
        fout = open("data.txt", "wt", encoding="utf8")
        str_ = heading + '_&_' + link_ + '_&_' + text
        fout.write(str_)
        fout.close()
        create_si()
        return render_template('return.html')


@app.route('/topic/si/<int:number>')
def topic_si(number):
    con = sqlite3.connect("db/scammers_in_the_internet.db")
    cr = con.cursor()
    link_ = cr.execute("""SELECT LINK FROM internet
                WHERE NUMBER > 0""").fetchall()
    text = cr.execute("""SELECT TEXT FROM internet
                WHERE NUMBER > 0""").fetchall()
    for i in range(len(link_)):
        link_[i] = str(link_[i])[2:-3]
    for i in range(len(text)):
        text[i] = str(text[i])[2:-3]
    number = int(number) - 1
    return render_template('topic_si.html', number=number, link=link_, text=text)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
