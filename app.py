from xml.sax import default_parser_list
from flask import Flask, render_template, jsonify
from database import load_posts_from_db, load_post_from_db
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()


# def load_posts_from_db():
# with engine.connect() as connection:
# result = connection.execute(text("SELECT * FROM posts"))

# posts = []
# for row in result.all():
# posts.append(dict(row))
# return posts


@app.route("/")
def hello_world():
    posts = load_posts_from_db()
    return render_template('home.html',
                           posts=posts)


@app.route("/api/posts")
def list_posts():
    posts = load_posts_from_db()
    return jsonify(posts)

@app.route("/post/<id>")
def show_post(id):
    post = load_post_from_db(id)
    return jsonify(post)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
