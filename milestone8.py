import csv
from collections import defaultdict
from operator import attrgetter

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f"{self.title} by {self.author}"

class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=attrgetter('title'))

class Bookshelf:
    def __init__(self):
        self.shelves = defaultdict(Shelf)

    def add_shelf(self, shelf):
        self.shelves[len(self.shelves)] = shelf

    def organize_books_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['Title']
                author = row['Author']
                category = row['Category']
                book = Book(title, author, category)
                self.shelves[category].add_book(book)

    def sort_books_in_shelves(self):
        for shelf in self.shelves.values():
            shelf.sort_books()

# Example usage
if __name__ == "__main__":
    bookshelf = Bookshelf()
    bookshelf.organize_books_from_csv('books_catalog.csv')
    bookshelf.sort_books_in_shelves()

    for category, shelf in bookshelf.shelves.items():
        print(f"Shelf {category}:")
        for book in shelf.books:
            print(f"- {book}")
