import sqlite3
from aifc import Error

import flask
from flask import request, Flask

app = Flask(__name__)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM produktinformationen")

    rows = cur.fetchall()

    return flask.jsonify(rows)

def create_project(conn, project):


    sql = "INSERT INTO einkaufsliste(Produkt,Mitglied,Menge) VALUES(?, ?, ?);"
    cur = conn.cursor()
    cur.execute(sql, project )
    conn.commit()
    return ""

@app.route('/login')
def login():
    error = None
    create_connection("datenbank.db")
    return request.args.get('name')


@app.route('/einkaufsliste/hinzufuegen')
def eink_hinzu():
    error = None
    einkaufsliste = create_connection("datenbank.db")
    a = request.args.get("Produkt")
    b = request.args.get("Mitglied")
    c = request.args.get("Menge")
    return create_project(einkaufsliste, (a, b, c))

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port='8000', debug=True)

