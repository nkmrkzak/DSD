# @title ch07-ex02
# UTF-8を使い、mysteryをpop_bytesというbytes変数にエンコードしよう。
# そして、pop_bytesを表示しよう。
mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

# result:
# b'\xf0\x9f\x92\xa9'
