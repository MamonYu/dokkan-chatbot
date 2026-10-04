from flask import Flask, jsonify
from queries import get_all_units_with_categories

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(get_all_units_with_categories())
   

app.run()