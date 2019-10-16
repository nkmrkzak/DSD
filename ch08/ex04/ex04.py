import csv

with open('books.csv', 'rt') as fp:
    books = csv.DictReader(fp)
    for book in books:
        print(book)

# OrderedDict([('author', 'J R R Tolkien'), ('book', 'The Hobbit')])
# OrderedDict([('author', 'Lynne Truss'), ('book', 'Eats, Shoots & Leaves')])
