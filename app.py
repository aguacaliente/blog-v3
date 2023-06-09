from crypt import methods
from email.mime import application
from xml.sax import default_parser_list
from flask import Flask, render_template, jsonify, request
from database import load_posts_from_db, load_post_from_db



app = Flask(__name__)



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
    if not post:
        return "No post found", 404
    return render_template('postpage.html', 
                           post=post)
    
@app.route("/post/<id>/comment", methods =['post'])
def send_comment(id):
    data = request.form
    return render_template('comment_submitted.html', 
                           comment=data)




if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
