import os
from datetime import datetime
from flask import Flask , render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Password1!@localhost/demo_app_db'

db = SQLAlchemy(app)


class MovieDb(db.Model):
	id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
	movietitle = db.Column(db.String(80),nullable=False)
	genre = db.Column(db.String(200),nullable=False)
	director= db.Column(db.String(200),nullable=False)
	rating= db.Column(db.Integer)
	star= db.Column(db.String(500),nullable=False)
	releaseDate= db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

	def __init__(self,movietitle,genre,director,rating,star,releaseDate):
		self.movietitle=movietitle
		self.genre=genre
		self.director=director
		self.rating=rating
		self.star=star
		self.releaseDate=releaseDate

	def __repr__(self):
		return  '<MovieTitle {}>'.format(self.movietitle)



@app.route('/')
def home():
	 return "Home"

@app.route('/about')
def home():
	 return "About"

@app.route('/contact')
def home():
	 return "Contact"

@app.route('/movies',methods=["POST","GET"])
def movies():
	movies = MovieDb(request.form['movietitle'],request.form['genre'],request.form['director'],request.form['rating'],request.form['star'],request.form['releaseDate'])
	db.session.add(movies)
	db.session.commit()
	movies = MovieDb.query.all()
	return render_template('movie.html',movies=movies)
	

if __name__ == '__main__':
	app.run(debug=True)