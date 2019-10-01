import sys
import pathlib
import re

# ディレクトリの絶対パスを取得
current_dir = pathlib.Path(__file__).resolve().parent
# モジュールのあるパスを追加
sys.path.append(str(current_dir) + '/../')
from mammoth import mammoth

# \b: 単語の境界
# \w: 単語(文字と数字とアンダースコア)
#  *: 0個以上の繰り返し
print(re.findall(r'\bc\w*\b', mammoth))
#  r: rawの意味、\をエスケープさせないためにつける
