from faker import Faker
import csv

fake = Faker()

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f"{self.title}, {self.author}, {self.category}"

def generate_books(num_books):
    books = []
    for _ in range(num_books):
        title = fake.catch_phrase()
        author = fake.name()
        category = fake.random_element(elements=("Dystopian Fiction", "Classic Fiction", "Coming-of-age Fiction"))
        books.append(Book(title, author, category))
    return books

def save_books_to_csv(books, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Category"])
        for book in books:
            writer.writerow([book.title, book.author, book.category])

if __name__ == "__main__":
    num_books = 10
    books = generate_books(num_books)
    save_books_to_csv(books, "books_catalog.csv")
