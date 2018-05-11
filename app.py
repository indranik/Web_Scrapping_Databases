
# import necessary libraries
from flask import Flask, render_template,jsonify,redirect
import pymongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.Mars_db
collection = db.Mars_facts
db.Mars_facts.remove()

@app.route("/scrape")
def scrape():
    finalresults = scrape_mars.scrape()
    db.Mars_facts.insert_one(finalresults)
    return (redirect("/"))

# create route that renders index.html template
@app.route("/")
def home():
    finalresults = list(db.Mars_facts.find())
    print(finalresults)



    return render_template("index.html", finalresults=finalresults)


if __name__ == "__main__":
    app.run(debug=True)
