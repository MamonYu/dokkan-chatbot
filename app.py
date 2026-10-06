from flask import Flask, jsonify , request 
from queries import get_all_units_with_categories , get_units_by_category , find_matches_sql

app = Flask(__name__)

@app.route("/units")
def all_units():
    return jsonify(get_all_units_with_categories())

@app.route("/units/category/<category_name>")
def units_by_category(category_name):
    return jsonify(get_units_by_category(category_name))
   
@app.route("/units/search")
def match_search():

    category =   request.args.get("category")
    rarity =     request.args.get("rarity")
    has_revive_check = request.args.get("has_revive")

    if has_revive_check is None:
        has_revive = False
    else :
        has_revive = str(has_revive_check).strip().lower() in ("true", "yes" , "1")


    search_output = find_matches_sql(category , rarity , has_revive)
    return jsonify(search_output)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error":"Route not found"}) , 404
    
if __name__ == "__main__":
    app.run(debug = True)