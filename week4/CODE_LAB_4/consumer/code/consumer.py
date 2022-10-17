
from flask import Flask,render_template
import requests
import os
import json


app = Flask(__name__)

@app.route('/',methods= ['GET'])
def index():
   
    #meal_item = response.text
    #return render_template('index.html', food=meal_item)

    #api_host = os.environ.get('API_HOST')
    #api_port = os.environ.get('API_PORT')
    #api_endpoint = os.environ.get('API_ENDPOINT')
    #url = f'http://{api_host}:{api_port}/{api_endpoint}'

    response = requests.get('http://api:5000/meal')
    recommend = json.loads(response.text)
    return render_template('home.html',meal_name=recommend['foodName'],meal_price=recommend['price'])



if __name__ == "__main__":
    
    port = os.environ.get("${CONSUMER_PORT}",'80')
    app.run(host='0.0.0.0', port=port,debug=True)
