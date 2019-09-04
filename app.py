from flask import Flask, render_template, jsonify
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '6\xabQ\x1f\xe8\xf3;\\,sW\x08\xb6\xff\xaecGO9\xadN[\xa7\xbf'


@app.route('/')
def home():
    with open("json/books.json", mode='r', encoding='utf-8') as books:
        data = json.load(books)
    return render_template('index.html', books=data['books'])


@app.route('/book/<int:book_id>')
def show_book_details(book_id):
    with open("json/books.json", mode='r', encoding='utf-8') as books:
        data = json.load(books)
        for book in data['books']:
            if book['id'] == book_id:
                item = book
    return render_template("book_detail.html", book=item)


if __name__ == "__main__":
    app.run(debug=True)