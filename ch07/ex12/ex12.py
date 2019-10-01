import sys
import pathlib
import binascii

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from gif import s

gif = binascii.unhexlify(s)
print(gif)
