import sqlite3
import csv

with sqlite3.connect('books.db') as conn:
    curs = conn.cursor()
    with open('books.csv', 'rt') as fin:
        books = csv.DictReader(fin)
        for contents in books:
            curs.execute('insert into book values( "{0}", "{1}", "{2}" )'.format(
                contents['title'], contents['author'], contents['year']))

    conn.commit()
    curs.execute('SELECT * FROM book')
    print(curs.fetchall())

    curs.close()

#
# result
#
#  [
# ('The Weirdstone of Brisingamen', 'Alan Garner', 1960),
# ('Perdido Street Station', 'China Mieville', 2000),
# ('Thud!', 'Terry Pratchett', 2005),
# ('The Spellman Files', 'Lisa Lutz', 2007),
# ('Small Gods', 'Terry Pratchett', 1992)
# ]
