import redis

conn = redis.Redis()
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})

print(conn.hgetall('test'))

# result
# {b'count': b'1', b'name': b'Fester Bestertester'}
