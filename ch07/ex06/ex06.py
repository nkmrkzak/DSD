# @title ch07-ex06
# salutation, name, product, verbed, room, animals, amount, percent, spokesman, job_title
# という文字列キーに値を追加して、responseという辞書を作ろう。
# そして、responseの値を使ってletterを表示しよう
letter = '''
Dear {salutation} {name}, 

Thank you for your letter. We are sorry that our {product} {verbed} in your 
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send 
you another {product} that, in our tests, is {percent}% less likely to 
have {verbed}.

Thank you for your support.

Sicerely,
{spokesman}
{job_title}
'''
response = {
    'salutation': 'a',
    'name': 'b',
    'product': 'c',
    'verbed': 'd',
    'room': 'e',
    'animals': 'f',
    'amount': 'g',
    'percent': 'h',
    'spokesman': 'i',
    'job_title': 'j'
}
print(letter.format(**response))

# result:
'''
Dear a b,

Thank you for your letter. We are sorry that our c d in your
e. Please note that it should never be used in a e, especially
near any f.

Send us your receipt and g for shipping and handling. We will send
you another c that, in our tests, is h% less likely to
have d.

Thank you for your support.

Sicerely,
i
j
'''
