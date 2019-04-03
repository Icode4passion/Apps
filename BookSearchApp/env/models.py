from app import db

class BooksDB(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	book_title = db.Column(db.String)
	book_type = db.Column(db.String)
	authors = db.Column(db.String)
	UID = db.Column(db.Integer)
	publisher = db.Column(db.String)
	publish_date = db.Column(db.Integer)
	edition = db.Column(db.String)
	binding = db.Column(db.String)
