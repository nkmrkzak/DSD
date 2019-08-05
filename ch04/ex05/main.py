"""4-5
辞書内包表記を使って、squares という辞書を作ろう。ただし、range(10) を使っ てキーを返し、各キーの自乗をその値とする。
"""

def chapter4_exam5():
    squares = {key: key ** 2 for key in range(10)}
    print(squares)

if __name__ == "__main__":
    chapter4_exam5()
