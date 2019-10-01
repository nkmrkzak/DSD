# @title ch07-ex05
# 新しいスタイルの書式指定を使って定形書簡を作りたい。
# 次の文字列をletterという変数に保存しよう
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
print(letter)

# result:
'''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent} % less likely to
have {verbed}.

Thank you for your support.

Sicerely,
{spokesman}
{job_title}
'''
