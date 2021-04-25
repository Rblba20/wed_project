import sqlite3


def create():
    data = open("data.txt", 'r', encoding='utf8').read()
    data = data.split('_&_')
    con = sqlite3.connect("db/phone_scammers.db")
    cr = con.cursor()
    cr.execute("""INSERT INTO phones(DATETIME,PHONE,TEXT,REGION) VALUES(?,?,?,?)""",
               (data[0], data[1], data[2].strip(), data[3]))
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
    con.commit()
    con.close()
    print(numbers, phones, texts, datetimes, regions)
