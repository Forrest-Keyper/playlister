from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

'''
# OUR MOCK ARRAY OF PROJECTS
playlists = [
    {'title': 'Cat Videos', 'description': 'Cats acting weird'},
    {'title': '80\'s Music', 'description': 'Don\'t stop believing!'}
]
'''


@app.route('/')
def playlists_index():
    """Show all playlists."""
    # find() method returns an iterable of all playlists in our database
    return render_template('playlists_index.html', playlists=playlists.find())


@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))


@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html')


if __name__ == '__main__':
    app.run(debug=True)
