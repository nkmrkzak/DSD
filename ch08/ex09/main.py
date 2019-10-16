import sqlite3

with sqlite3.connect('books.db') as conn:
    curs = conn.cursor()

    curs.execute('SELECT * FROM book ORDER BY year')
    print(curs.fetchall())

    curs.close()

#
# result
#
# [
# ('The Weirdstone of Brisingamen', 'Alan Garner', 1960),
# ('Small Gods', 'Terry Pratchett', 1992),
# ('Perdido Street Station', 'China Mieville', 2000),
# ('Thud!', 'Terry Pratchett', 2005),
# ('The Spellman Files', 'Lisa Lutz', 2007)]
