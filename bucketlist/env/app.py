from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
	return "Home"

@app.route('/about')
def home():
	return "About"


@app.route('/contact')
def home():
	return "Contact"


if __name__ == '__main__':
	app.run(debug=True)