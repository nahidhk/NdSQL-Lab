import sys
import os

# parent folder add করা
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def connect_db(dbname):
    return mysql.connector.connect(
        host=config.DB_CONFIG["host"],
        user=config.DB_CONFIG["user"],
        password=config.DB_CONFIG["password"],
        database=dbname
    )


@app.route("/get/db=<dbname>&tb=<tbname>&key=<key>")
def get_data(dbname, tbname, key):

    if key != config.API_KEY:
        return jsonify({"error": "Invalid API key"})

    try:
        db = connect_db(dbname)
        cursor = db.cursor(dictionary=True)

        query = f"SELECT * FROM {tbname}"
        cursor.execute(query)

        data = cursor.fetchall()

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(port=5000, debug=True)