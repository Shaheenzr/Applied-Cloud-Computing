
from flask import Flask,jsonify
import random

app = Flask(__name__)
 
meals=[ {'foodName':'Chicken korma', 'price':15.00},
        {'foodName':'Mongolian beef', 'price':16.00},
        {'foodName':'Hunan chicken', 'price':14.00},
        {'foodName':'Tomato soup', 'price':10.00},
        {'foodName':'Lamb cumin', 'price':18.50},
        {'foodName':'Bean Cheese Burrito','price':10.75 },
        {'foodName':'Schezwan Fried rice', 'price':12.00},
        {'foodName':'Hakka noodles', 'price':14.00},
        {'foodName':'pizza', 'price':8.00},
        {'foodName':'burger', 'price':5.50},
        {'foodName':'Ramen', 'price':14.75},
        {'foodName':'Taco', 'price':4.54},
        {'foodName':'Vegan Thai curry', 'price':12.56 },
        {'foodName':'White Rice', 'price':3.50 },
        {'foodName':'Sauerbraten', 'price':14.50 },
        {'foodName':'Gulasch', 'price':16.75 }  ]

@app.route('/')
def home_page():
    s = "Hello There! are you hungry?? choose your meals"
    return s

@app.route("/menu",methods = ['GET'])
def food_dictionary():
   return jsonify({"food":meals})

@app.route('/meal',methods= ['GET'])
def random_selection():
    random_index= random.randint(0,15)
    return meals[random_index]    

if __name__ == "__main__":
    app.run('0.0.0.0', port = 5000,debug=True)


