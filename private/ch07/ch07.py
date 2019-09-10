print("7-1")
import unicodedata
mystery = '\U0001f4a9'

print(mystery)
print(unicodedata.name(mystery))

print("7-2")
pop_bytes = mystery.encode('utf-8')

print(pop_bytes)

print("7-3")
pop_string = pop_bytes.decode('utf-8')

print(pop_string)
print(mystery == pop_string)

print("7-4")
s = "My kitty cat likes %s," \
    "My kitty cat likes %s," \
    "My kitty cat fell on his %s," \
    "And now thinks he's a %s." % ("roast beef", "ham", "head", "clam")

print(s)

print("7-5")
letter = "Dear {salutation} {name}"

print("7-6")
print(letter.format(salutation="Mr.", name="aaa"))

print("7-7")
mammoth = '''
    We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare seize.

    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.

    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.

    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great world's show at Paris.

    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs or glees
    We could not sing, oh! queen of cheese.

    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon.'''

print(mammoth)

print("7-8")
import re
print(re.findall(r'\bc\w*\b', mammoth))

print("7-9")
print(re.findall(r'\bc\w{3}\b', mammoth))

print("7-10")
print(re.findall(r'\b\w*r\b', mammoth))

print("7-11")
print(re.findall(r'\b\w*[aiueo]{3}[^aiueo\s]*\w*\b', mammoth))

print("7-12")
import binascii
s = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'

gif = binascii.unhexlify(s)
print(gif)

print("7-13")
print(gif[:6] == b'GIF89a')

print("7-14")
import struct
width, height = struct.unpack("<HH", gif[6:10])
print(f'{width} {height}')
