import sqlite3
from aifc import Error

import flask
from flask import request, Flask

app = Flask(__name__)


@app.route('/')
def hello_world82():
    return 'Welcome to Smart Groceries'


@app.route('/shoppinglist')
def hello_world2():
    error = None
    conn = create_connection("datenbank.db")
    return select_all_tasks(conn)


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM produktinformationen;")

    rows = cur.fetchall()

    return flask.jsonify(rows)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM produktinformationen", (priority,))

    rows = cur.fetchall()

    return flask.jsonify(rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
