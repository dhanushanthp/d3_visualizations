import json

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

file = open('word_groups.csv', 'r') 
data = file.read()

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/get_data')
def parse_request():
    return data


if __name__ == "__main__":
    app.run(debug=True)