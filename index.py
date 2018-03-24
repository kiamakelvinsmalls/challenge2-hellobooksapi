from flask import Flask,jsonify,abort,request
app=Flask(__name__)
books=[
{
"id":1,
"bookname":"a niggas life",
"author":"kelvin kiama",
"category":"drama,action",
"quantity":10
	
},
{
"id":2,
"bookname":"life in the hood",
"author":"kelvin kiama",
"category":"drama,action",
"quantity":10
	
}
]
#get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

#get book by id

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book["id"] ==book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'books': books[0]})


@app.route('/books', methods=['POST'])
def add_book():
	book = {
	'id': request.json['id'],
	'bookname': request.json['bookname'],
	'author': request.json['author'],
	'category': request.json['category'],
	'quantity': request.json['quantity']
	}
	books.append(book)
	return jsonify({'book': book}), 201
if __name__=="__main__":
	app.run()