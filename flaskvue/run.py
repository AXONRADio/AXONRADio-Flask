from flask import Flask, render_template
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

'''
@app.route('/api/song', methods=['GET'])
def get_all_songs():
    songs = mongo.db.posts
    output = []
    for q in songs.find():
        output.append({"name": q['name'], "genre": q['genre'], "url": q['url']})
    return jsonify(output)

@app.route('/api/song/<genre>/', methods=['GET'])
def get_song_list(genre):
    songs = mongo.db.posts
    output = []
    for q in songs.find({"genre": genre}).limit(10):
        output.append({"name": q['name'], "genre": q['genre'], "url": q['url'], "vidID":q['vidID']})
    return jsonify(output)

@app.route('/api/song/one/<genre>', methods=['GET'])
def get_one_song(genre):
    songs = mongo.db.posts.find_one({"genre": genre})
    return jsonify({"name": songs['name'], "genre": songs['genre'], "url": songs['url']})

@app.route('/api/video/<genre>/', methods=['GET'])
def get_one_video(genre):
    songs = mongo.db.posts.find_one({"genre": genre})
    return songs['vidID']

'''


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
