 
from app import app
from db_setup import init_db, db_session
from forms import BookSearchForm ,AddBooksForm
from flask import flash, render_template, request, redirect
from models import BooksDB

init_db()


@app.route('/',methods=["POST","GET"])
def index():
	search = BookSearchForm(request.form)
	if request.method == "POST":
		return search_results(search)
	return render_template('index.html',form = search)


@app.route('/results')
def search_results(search):
	results = []
	search_string = search.data['search']
	print(search_string)

	if search_string:
		query = db_session.query(BooksDB).filter(BooksDB.authors.contains(search_string))
		results = query.all()
		return render_template('search_result.html',results=results)

		#print(results.data)


	else:
		qry = db_session.query(BooksDB)
		results = qry.all()

	if not results:
		flash('No results found')
		return redirect('/')

	else :
		posts = BooksDB.query.all() 
		return render_template('results.html',posts=posts)


@app.route('/new_book',methods=["POST","GET"])
def new_book():
	form = AddBooksForm(request.form)
	if request.method == "POST":
		booksdb = BooksDB()
		save_changes(booksdb,form,new=True)
		flash("Book Added Successfully")
		return redirect('/')
	return render_template('new_books.html',form=form)

def save_changes(booksdb,form,new=False):
	booksdb.book_title = form.book_title.data
	booksdb.book_type  =form.book_type.data
	booksdb.authors  = form.authors.data
	booksdb.UID  = form.UID.data
	booksdb.publisher  = form.publisher.data
	booksdb.publish_date= form.publish_date.data
	booksdb.edition  = form.edition.data
	booksdb.binding= form.binding.data

	if new :
		db_session.add(booksdb)

	db_session.commit()



if __name__ == '__main__':
	app.run(debug=True)
