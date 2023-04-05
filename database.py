

from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"}})


def load_posts_from_db():
    with engine.connect() as connection:
     result = connection.execute(text("SELECT * FROM posts"))
    
     posts = []
     for row in result.all():
        posts.append(dict(row))
     return posts