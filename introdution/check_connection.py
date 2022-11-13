from redis import Redis

client = Redis("192.168.1.7", 6379, 1)

# ping()方法在连接正常时将返回TRUE
if client.ping() is True:
    print("Connecting")
else:
    print("disconnected")