from flask import render_template, request, redirect
from app import app
from models.bookshop import booklist, add_new_book, remove_book
from models.book import *

@app.route('/bookshop')
def index():
    return render_template('index.html', title = 'Home', booklist = booklist)

@app.route('/bookshop', methods = ['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = True if 'checked_out' in request.form else False

    new_book = Book(title, author, genre, checked_out)

    add_new_book(new_book)

    return redirect('/bookshop')

@app.route('/bookshop/<title>')
def view_book(title):

    book = None

    for book in booklist:
        if book.title == title:
            book = book
            break
    return render_template('book.html', book = book, title = title)

@app.route('/bookshop/<title>', methods = ['POST'])
def delete_book(title):

    remove_book(title)
    return redirect('/bookshop')