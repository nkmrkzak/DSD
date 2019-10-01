# @title ch07-ex04
# 古いスタイルの書式指定を使って次の詩を表示し、置換部分に'roast beef'、'ham'、'head'、'clam'を挿入しよう
song = '''My kitty cat likes %s, 
My kitty cat likes %s, 
My kitty cat fell on his %s 
And now thinks he\'s a %s.
    '''
words = ('roast beef', 'ham', 'head', 'clam')
print(song % words)

# result:
# My kitty cat likes roast beef,
# My kitty cat likes ham,
# My kitty cat fell on his head
# And now thinks he's a clam.
