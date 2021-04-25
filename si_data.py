import sqlite3


def create_si():
    data = open("data.txt", 'r', encoding='utf8').read()
    data = data.split('_&_')
    con = sqlite3.connect("db/scammers_in_the_internet.db")
    cr = con.cursor()
    cr.execute("""INSERT INTO internet(LINK,TEXT,HEADING) VALUES(?,?,?)""",
               (data[1], data[2].strip(),  data[0]))
    number = cr.execute("""SELECT NUMBER FROM internet
            WHERE NUMBER > 0""").fetchall()
    link_ = cr.execute("""SELECT LINK FROM internet
            WHERE NUMBER > 0""").fetchall()
    text = cr.execute("""SELECT TEXT FROM internet
            WHERE NUMBER > 0""").fetchall()
    heading = cr.execute("""SELECT HEADING FROM internet
            WHERE NUMBER > 0""").fetchall()
    con.commit()
    con.close()
    print(number, link_, text, heading)
