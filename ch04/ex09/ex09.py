# @title ch04-09
def get_odds():
    for number in range(1, 10, 2):
        yield number


for i, odd in enumerate(get_odds(), 1):
    if i == 3:
        print(odd)

# result:
# 5
