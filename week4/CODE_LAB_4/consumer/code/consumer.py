
from flask import Flask,render_template
import requests
import os
import json

#took reference from below resources
# https://stackoverflow.com/questions/39579666/how-to-set-background-image-on-flask-templates
# https://pythonbasics.org/flask-template-data/
# https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html
# https://dzone.com/articles/build-deploy-flask-application-using-docker
# https://towardsdatascience.com/a-series-on-flask-apis-part-1-getting-and-posting-33985dfe8816

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def index():
    response = requests.get('http://api:5000/meal')
    recommend = json.loads(response.text)
    return render_template('home.html',meal_name=recommend['foodName'],meal_price=recommend['price'])

if __name__ == "__main__":
    
    port = os.environ.get("${CONSUMER_PORT}",'80')
    app.run(host='0.0.0.0', port='80',debug=True)
