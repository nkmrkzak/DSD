# @title ch07-ex01
# mysteryというUnicode文字列を作り、'\U0001f4a9'という値を代入して、mysteryを表示してみよう。
# またmysteryのUnicode名を調べよう
import unicodedata
mystery = '\U0001f4a9'
print(mystery)
print(unicodedata.name(mystery))

# result:
# 💩
# PILE OF POO
# ※import文をファイルの途中に書くと、pylintが勝手にファイルの先頭に移動してくれる
