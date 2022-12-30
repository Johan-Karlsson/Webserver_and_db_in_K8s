import psycopg as p
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    connection = p.connect(
        host=os.environ.get('POSTGRES_SERVICE_SERVICE_HOST'),
        port=os.environ.get('POSTGRES_SERVICE_SERVICE_PORT'),
        dbname=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD')
    )

    # create a cursor
    cursor = connection.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cursor.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cursor.fetchone()

    # close the communication with the PostgreSQL
    cursor.close()

    connection.close()
    return {"db_version": db_version}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)