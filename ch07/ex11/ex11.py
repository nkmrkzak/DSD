import sys
import pathlib
import re

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from mammoth import mammoth

# \b: 単語の境界
# \w: 単語(文字と数字とアンダースコア)
#  *: 0個以上の繰り返し
# {n}: n回繰り返し
# \s: 空白
print(re.findall(r'\b\w*[aiueo]{3}[^aiueo\s]*\w*\b', mammoth))

