"""4-6
集合内包表記を使って、range(10) の奇数から odd という集合を作ろう。
"""

def chapter4_exam6():
    odd = {number for number in range(10) if number % 2 == 1}
    print(odd)

if __name__ == "__main__":
    chapter4_exam6()
