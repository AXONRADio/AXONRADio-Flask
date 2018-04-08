from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from string import Template
import bcrypt
import requests

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongoAXONRADio'
app.config['MONGO_URI'] = 'mongodb://localhost'

mongo = PyMongo(app)

HTML_TEMPLATE = Template("""
<!DOCTYPE html>
<head>
   <title>My Video App</title>
</head>
<body>
    <h2>${headline}</h2>

    <iframe src="https://www.youtube.com/embed/${youtube_id}?autoplay=1" frameborder="0" allowfullscreen></iframe>
</body>""")


@app.route("/")
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                         login_user['password'].encode('utf-8')) == login_user[
                             'password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                                     bcrypt.gensalt())
            users.insert({
                'name': request.form['username'],
                'password': hashpass
            })
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


@app.route('/videos/<vid>')
def videos(vid):
    youtube_url = 'https://www.youtube.com/watch?v=' + vid
    if True == is_url_ok(youtube_url):
        hed = """<a href="{url}">YouTube video: {id}</a>""".format(
            url=youtube_url, id=vid)
        all_html = HTML_TEMPLATE.substitute(headline=hed, youtube_id=vid)
    else:
        hed = """YouTube video <u>{id}</u> does not exist""".format(id=vid)
        all_html = HTML_TEMPLATE.substitute(
            headline=hed, youtube_id='ohQPySWJToo')

    return all_html


def is_url_ok(url):
    return 200 == requests.head(url).status_code

if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(debug=True, use_reloader=True)
