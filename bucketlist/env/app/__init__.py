from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request , jsonify , abort



from instance.config import app_config

db = SQLAlchemy()


def create_app(config_name):
	from app.models import Bucketlist
	app = FlaskAPI(__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
	db.init_app(app)


	return app



	@app.route('/bucketlists/',methods=['GET','POST'])
	def bucketlist():
		if request.method == 'POST':
			name = str(request.data.get('name',''))
			if name:
				bucketlist = Bucketlist(name=name)
				bucketlist.save()
				response  = jsonify({
					'id':bucketlist.id,
					'name':bucketlist.name,
					'date_created':bucketlist.date_created,
					'date_modified':bucketlist.date_modified
					})
				response.status_code = 201
				return response


			else:
				bucketlists = Bucketlist.get_all()
				result = []

				for bucketlist in bucketlists:
					obj = {
					'id':bucketlist.id,
					'name':bucketlist.name,
					'date_created':bucketlist.date_created,
					'date_modified':bucketlist.date_modified

					}
					result.append(obj)
				response=jsonify(result)
				response.status_code=200
				return response
		return app
