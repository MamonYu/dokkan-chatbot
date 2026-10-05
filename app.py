from flask import Flask, jsonify
from queries import get_all_units_with_categories , get_units_by_category

app = Flask(__name__)

@app.route("/units/category/<category_name>")
def units_by_category(category_name):
    return jsonify(get_units_by_category(category_name))
   

app.run()