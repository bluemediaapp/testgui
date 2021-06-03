from flask import Flask, render_template
from pymongo import MongoClient
from json import dumps

app = Flask(__name__)
client = MongoClient()
blue = client["blue"]

@app.route("/")
def index():
    return render_template("index.jinja2")

@app.route("/db/show/<string:database>")
def explore_db(database):
    return dumps(list(blue[database].find()))
@app.route("/db/clear/<string:database>")
def clear_db(database):
    blue[database].delete_many()
    return ""
app.run("0.0.0.0", debug=True)
