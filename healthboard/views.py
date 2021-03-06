 
from flask import render_template, jsonify
from healthboard import app
from healthboard.data import data



# home route
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/data")
def get_data():
    return jsonify(data)



