from flask import Flask, render_template
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
if __name__ == '__main__':
    app.run(debug=True)
