from flask import Flask , request ,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os


#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


db = SQLAlchemy(app)
ma = Marshmallow(app)


class Movie(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(100),unique=True)
	director = db.Column(db.String(100))
	production = db.Column(db.String(100))
	rating = db.Column(db.Integer)
	release = db.Column(db.Integer)

	def __init__(self,title,director,production,rating,release):
		
		self.title= title
		self.director= director
		self.production= production		
		self.rating= rating
		self.release= release


#product schema

class MovieSchema(ma.Schema):
	class Meta:
		fields = ('id',
					'title',
					'director',
					'production',
                                        'rating',
					'release'
					)



# init schema
movie_schema = MovieSchema(strict=True)
movies_schema = MovieSchema(many=True,strict=True)



#create a movie

@app.route('/movie',methods=['POST'])
def add_movie():
	title = request.json['title']	
	director= request.json['director']
	production=request.json['production']
	rating=request.json['rating']
	release=request.json['release']
	

	new_movie = Movie(title,director,production,release,rating)

	db.session.add(new_movie)
	db.session.commit()


	return movie_schema.jsonify(new_movie)


#get all products

@app.route('/movie',methods=['GET'])
def get_movie():
	all_movies = Movie.query.all()
	result = movies_schema.dump(all_movies)
	return jsonify(result.data)


#update movie


@app.route('/movie/<id>',methods=['PUT'])
def update_movie(id):

	movie = Movie.query.get(id)

	title = request.json['title']	
	director= request.json['direction']
	production=request.json['production']
	rating=request.json['rating']
	release=request.json['release']
	

	
	movie.title = title
	movie.director=director
	movie.production=production
	movie.rating=rating
	movie.release=release
	


	db.session.commit()


	return movie_schema.jsonify(movie)


#





if __name__ == '__main__':
	app.run(debug=True)
