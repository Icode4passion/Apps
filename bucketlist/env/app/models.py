from app import db

class Bucketlist(db.Model):
	__tablename__ = "bucketlist"

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(128))
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


	def __init__(self,name):
		self.name = name


	def save(self):
		db.session.add(self)
		db.session.commit()


	@staticmethod
	def get_all(self):
		return Bucketlist.query.all()

	def delete(self):
		d.session.delete(self)
		db.session.commit()


	def __repr__(self):
		return "Bucketlist: {}".format(self.name)


