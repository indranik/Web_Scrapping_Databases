from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    FinalResults = mongo.db.FinalResults.find_one()
    return render_template("index.html", FinalResults=FinalResults)


@app.route("/scrape")
def scrape():
    FinalResults = mongo.db.listings
    FinalResults_data = scrape_mars.scrape()
    FinalResults.update(
        {},
        FinalResults_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
