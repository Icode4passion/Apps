from flask import Flask 

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mybook.db"
app.secret_key = "Rock Flask"

db = SQLAlchemy(app)