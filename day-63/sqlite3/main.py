# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
print("Passing by here")
db.init_app(app)


with app.app_context():
    db.create_all()


# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()



with app.app_context():
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books.all())


book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
    book_to_update = db.get_or_404(Book, book_id)
    print(book_to_update.title)


book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
