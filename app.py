#from flask import Flask, render_template, jsonify, redirect
#from flask_pymongo import PyMongo
#import scrape_mars
#
#app = Flask(__name__)
#
#mongo = PyMongo(app)
#
#
#@app.route("/")
#def index():
#    FinalResults = mongo.db.FinalResults.find_one()
#    return render_template("index.html", FinalResults=FinalResults)
#
#
#@app.route("/scrape")
#def scrape():
#    FinalResults = mongo.db.FinalResults
#    FinalResults_data = scrape_mars.scrape()
#    FinalResults.update(
#        {},
#        FinalResults_data,
#        upsert=True
#    )
#    return redirect("http://localhost:5000/", code=302)
#
#
#if __name__ == "__main__":
#    app.run(debug=True)
# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.Mars_db
collection = db.Mars

@app.route("/scrape")
def scrape():
    finalresults = scrape_mars.scrape()
    db.collection.insert_one(finalresults)
    return "Scraped some data"

# create route that renders index.html template
@app.route("/")
def home():
    finalResults = list(db.collection.find())
    print(finalresults)



    return render_template("index.html", finalresults=finalresults)


if __name__ == "__main__":
    app.run(debug=True)
