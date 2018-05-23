import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://khamitkarsumit:Sumit1223@ds231720.mlab.com:31720/flsk_check")
db = client['flsk_check']
collection = db.FlaskCheck

@app.route('/')
def todo():
    _items = collection.find()
    items = [item for item in _items]
    return render_template('index.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }

    collection.insert_one(item_doc)

    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
