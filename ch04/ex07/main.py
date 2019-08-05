"""4-7
ジェネレータ内包表記を使って range(10) の数値に対しては、'Got ' と数値を返そう。for ループを使って反復処理すること。
"""

def chapter4_exam7():
    got_generator = (f'Got {number}' for number in range(10))
    for item in got_generator:
        print(item)

if __name__ == "__main__":
    chapter4_exam7()
