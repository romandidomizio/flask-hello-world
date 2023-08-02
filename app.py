import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab_10_database_user:UwufnvTL5ONEPaEj6UH6xZtOMTnjJeXL@dpg-cj4rd3icn0vc73fh7940-a/lab_10_database")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("your_db_url_here")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
