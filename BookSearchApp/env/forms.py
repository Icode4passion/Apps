from wtforms import Form , StringField , IntegerField,SelectField

class BookSearchForm(Form):
	search = StringField('')

class AddBooksForm(Form):
	book_types = [	('Default','Default'),
					('Education','Education'),
					('Kids','Kids'),
					('Programming','Programming'),
					('Education','Education'),
					('Art-Life','Art-Life')]

	publishers = [	('Others',"Others"),
					('Penguin Books India','Penguin Books India'),
					('HarperCollins Publishers India','HarperCollins Publishers India'),
					('Wiley India','Wiley India'),
					('Random House India','Random House India'),
					('Hachette India Publishers','Hachette India Publishers')]
	
	editions =[('None','None'),('First','First'),('Second','Second'),('Third','Third'),('Revised','Revised')]
	book_type = SelectField('Book Type',choices = book_types)
	book_title = StringField('Book Title')
	authors = StringField('Authors')
	UID = IntegerField('Unique Id')
	publisher = SelectField('Publisher',choices=publishers)
	publish_date = IntegerField('Published date')
	edition = SelectField('Edition',choices = editions)
	binding = StringField('Binding')