# @title ch04-10
def decorator(func):
    def decorated_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return decorated_func


@decorator
def test_func():
    print('test_func')


test_func()

# result:
# start
# test_func
# end
