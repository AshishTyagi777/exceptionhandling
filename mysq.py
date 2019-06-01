import sqlite3

conn = sqlite3.connect('tutorials.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix Real,datestamp TEXT,keyword TEXT,value REAL)")
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(2345872732329,'2016-02-02','pythonbasics',20)")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()
