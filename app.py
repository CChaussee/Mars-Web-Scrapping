from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = mars_facts

@app.route('/scrape')
def scrape:
    pleasework = scrape_mars.scrape()
    db.mars_facts.insert_one(pleasework)

@app.route('/')
def home():
    pleasework = db.mars_facts.find()
    return render_template ("index.html", pleasework = pleasework)

if __name__ == '__main__'
    app.run(debug =True)
    