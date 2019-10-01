import sys
import pathlib
import binascii
import struct

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from gif import s

gif = binascii.unhexlify(s)
width, height = struct.unpack("<HH", gif[6:10])
print(f'{width} {height}')

# おまけ
from construct import Struct, Const, Int16ul
fmt = Struct(
    "signature" / Const(b"GIF89a"),
    "width" / Int16ul,
    "height" / Int16ul,
)

result = fmt.parse(gif)
print(result)
