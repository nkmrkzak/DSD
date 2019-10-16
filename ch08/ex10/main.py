import sqlalchemy as sa

conn = sa.create_engine('sqlite:///books.db')

rows = conn.execute('SELECT title FROM book ORDER BY title')

for row in rows:
    print(row)

#
# result
#
# ('Perdido Street Station',)
# ('Small Gods',)
# ('The Spellman Files',)
# ('The Weirdstone of Brisingamen',)
# ('Thud!',)
