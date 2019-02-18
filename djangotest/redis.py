import redis

p = redis.ConnectionPool(host='127.0.0.1', port=6379)  # 连接池
r = redis.Redis(connection_pool=p)


# 操作redis的类
def IpMiddleware(ip):
    count = r.get(ip)  # 尝试获取ip的值
    if count is None or int(count) < 5:  # 不存在或者小于5
        pipe = r.pipeline(transaction=True)  # 管道
        r.incr(ip)  # ip++
        r.expire(ip, 60)  # 设置超时
        pipe.execute()  # 执行
        return True
    if int(count) > 5:
        return False
