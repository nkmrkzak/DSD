# @title ch07-ex03
# UTF-8を使ってpop_bytesを文字列変数pop_stringにデコードし、pop_stringを表示しよう。
# pop_stringはmysteryと等しいか？
mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(mystery == pop_string)

# result:
# 💩
# 等しい
