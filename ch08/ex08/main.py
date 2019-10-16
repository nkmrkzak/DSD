import sqlite3

with sqlite3.connect('books.db') as conn:
    curs = conn.cursor()

    curs.execute('SELECT title FROM book ORDER BY title')
    print(curs.fetchall())

    curs.close()

#
# result
# [
# ('Perdido Street Station',),
# ('Small Gods',),
# ('The Spellman Files',),
# ('The Weirdstone of Brisingamen',),
# ('Thud!',)]
