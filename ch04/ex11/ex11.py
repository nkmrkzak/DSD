# @title ch04-11
class OopsException(Exception):
    pass


try:
    raise OopsException()
except OopsException:
    print('Caught an oops')

# result:
# Caught an oops
