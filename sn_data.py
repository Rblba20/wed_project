import sqlite3


def create_sn():
    data = open("data.txt", 'r', encoding='utf8').read()
    data = data.split('_&_')
    con = sqlite3.connect("db/scammers_on_social_networks.db")
    cr = con.cursor()
    cr.execute("""INSERT INTO networks(LINK,TEXT,DATA,HEADING) VALUES(?,?,?,?)""",
               (data[1], data[3].strip(), data[2], data[0]))
    number = cr.execute("""SELECT NUMBER FROM networks
            WHERE NUMBER > 0""").fetchall()
    link_ = cr.execute("""SELECT LINK FROM networks
            WHERE NUMBER > 0""").fetchall()
    text = cr.execute("""SELECT TEXT FROM networks
            WHERE NUMBER > 0""").fetchall()
    date = cr.execute("""SELECT DATA FROM networks
            WHERE NUMBER > 0""").fetchall()
    heading = cr.execute("""SELECT HEADING FROM networks
            WHERE NUMBER > 0""").fetchall()
    con.commit()
    con.close()
    print(number, link_, text, date, heading)
