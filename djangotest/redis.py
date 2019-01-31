import redis

p = redis.ConnectionPool(host='127.0.0.1', port=6379) # 连接池
r = redis.Redis(connection_pool=p)


def IpMiddleware(ip):
    count = r.get(ip)
    if count == None or int(count) < 5:
        pipe = r.pipeline(transaction=True)
        r.incr(ip)
        r.expire(ip, 60)
        pipe.execute()
        return True
    if int(count) > 5:
        return False
