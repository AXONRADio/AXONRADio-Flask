from flask import Flask, jsonify, url_for, redirect, request, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests
from flask_cors import CORS
import random

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = CustomFlask(__name__,
                  static_folder = "../dist/static",
                  template_folder = "../dist")

cors = CORS(app, resources={r"/api/*": {"origins":"http://localhost:5000"}})
app.config['MONGO_DBNAME'] = 'song_db'
mongo = PyMongo(app, config_prefix='MONGO')

def jazz():
    count = mongo.db.jazz.count()
    return mongo.db.jazz.find()[random.randrange(count)]

def rock():
    count = mongo.db.rock.count()
    return mongo.db.rock.find()[random.randrange(count)]

def blues():
    count = mongo.db.blues.count()
    return mongo.db.blues.find()[random.randrange(count)]

def pop():
    count = mongo.db.pop.count()
    return mongo.db.pop.find()[random.randrange(count)]

def reggae():
    count = mongo.db.reggae.count()
    return mongo.db.reggae.find()[random.randrange(count)]

def hiphop():
    count = mongo.db.hiphop.count()
    return mongo.db.hiphop.find()[random.randrange(count)]

def disco():
    count = mongo.db.disco.count()
    return mongo.db.disco.find()[random.randrange(count)]

def country():
    count = mongo.db.country.count()
    return mongo.db.country.find()[random.randrange(count)]

def classical():
    count = mongo.db.classical.count()
    return mongo.db.classical.find()[random.randrange(count)]

def metal():
    count = mongo.db.metal.count()
    return mongo.db.metal.find()[random.randrange(count)]

def switch(arg):
    switcher = {
        'jazz': jazz,
        'rock': rock,
        'blues': blues,
        'pop': pop,
        'reggae': reggae,
        'hiphop': hiphop,
        'disco': disco,
        'country': country,
        'classical': classical,
        'metal': metal
    }
    func = switcher.get(arg, lambda:'invalid genre')
    return func()

# route to the static vue build or the local host
# when running on dev server
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

# endpoint for a random video query by genre
@app.route('/api/video/<genre>/', methods=['GET'])
def get_random_video(genre):
    ret = switch(genre)
    return jsonify({"name": ret['name'], "genre": ret['genre'], "vidID":ret['vidID'], "mean": ret['mean']})

# endpoint for the database count() content
@app.route('/api/data/', methods=['GET'])
def get_db_data():
    ret = [
        mongo.db.blues.count(),
        mongo.db.classical.count(),
        mongo.db.country.count(),
        mongo.db.disco.count(),
        mongo.db.hiphop.count(),
        mongo.db.jazz.count(),
        mongo.db.metal.count(),
        mongo.db.pop.count(),
        mongo.db.reggae.count(),
        mongo.db.rock.count()
    ]
    return jsonify(ret)
# make sure to remove debug mode in production
if __name__ == '__main__':
    app.run(debug=True)