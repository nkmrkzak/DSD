import os
import csv
import sqlite3
import sqlalchemy

print("8-1")
test1 = "This is a test of the emergency text system"
print(test1)

with open(os.getcwd() + "/text.txt", "wt") as fout:
    fout.write(test1)

print("8-2")
with open(os.getcwd() + "/text.txt", "rt") as fin:
    test2 = fin.read()

print(test1 == test2)

print("8-3")
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''

with open(os.getcwd() + "/books.csv", "wt") as fout:
    fout.write(text)

print("8-4")
with open(os.getcwd() + "/books.csv", "rt") as fin:
    books = csv.DictReader(fin)
    for book in books:
        print(book)

print("8-5")
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open(os.getcwd() + "/books.csv", "wt") as fout:
    fout.write(text)

print("8-6")
conn = sqlite3.connect("books.db")
curs = conn.cursor()
curs.execute('''CREATE TABLE book (title VARCHAR(20) , author VARCHAR(20), year INT)''')

conn.commit

print("8-7")
with open(os.getcwd() + "/books.csv", "r") as fin:
    cin = csv.DictReader(fin)
    for book in cin:
        print(book)
        curs.execute("INSERT INTO book values(?, ?, ?)", (book["title"], book["author"], book["year"]))
    conn.commit

print("8-8")
sql1 = "SELECT title FROM book ORDER BY title ASC"
for row in conn.execute(sql1):
    print(row)

print("8-9")
sql2 = "SELECT * FROM book ORDER BY year ASC"
for row in conn.execute(sql2):
    print(row)

print("8-10")
conn = sqlalchemy.create_engine("sqlite:///books.db")
for row in conn.execute(sql1):
    print(row)
