import redis

conn = redis.Redis()
print(conn.hincrby('test', 'count'))
print(conn.hincrby('test', 'count', 10))
print(conn.hincrby('test', 'count', 100))

# result
# 2
# 12
# 112
