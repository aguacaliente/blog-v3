from xml.sax import default_parser_list
from flask import Flask, render_template, jsonify

app = Flask(__name__)


POSTS = [
    {
    'id' : 1,
    'title': 'Quicker CSS with Bootstrap ',
    'author': 'John Doe',
    'tagline': ''
},
    {
    'id' : 2,
    'title': 'API endpoints ',
    'author': 'Jane Doe',
    'tagline': ''
},
    {
    'id' : 3,
    'title': 'React and CSS ',
    'author': 'Jane Doe',
    'tagline': ''
},
    {
    'id' : 4,
    'title': 'React and CSS ',
    'author': 'Betty Swallocks',
    'tagline': 'Common pitfalls when styling components in react'
},
    ]
@app.route("/")
def hello_world():
    return render_template('home.html',
                           posts=POSTS)
    
@app.route("/api/posts")
def list_posts():
    return jsonify(POSTS)



if __name__ == "__main__":
    app.run(host = "localhost", port =8080, debug=True)