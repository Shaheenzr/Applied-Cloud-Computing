from random import randint
from flask import Flask, jsonify
import json
import os
from sqlalchemy import create_engine

app = Flask(__name__)


db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('PG_USER')
db_pass = os.environ.get('PG_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('PG_PORT') 

db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db = create_engine(db_string)

def get_meal_records_from_db():
    query = "SELECT foodName,price FROM Meals ORDER BY RANDOM() LIMIT 1;"
    rows = db.execute(query)

    rowarray_list = []
    for row in rows:
        t = (row[0], row[1])
        rowarray_list.append(t)

    return list(rowarray_list)

@app.route('/')
@app.route('/recommendation/')
def index():
    return jsonify(get_meal_records_from_db())

app.run(host='0.0.0.0', port=os.environ.get('API_PORT'))