from redis import Redis

cache = Redis(host="redis", port=6379)
cache.set("example", 5)
cache.incr("times", 1)
print("SQRT: ", int(cache.get("example")) ** 2, "Incr: ", cache.get('times'))
