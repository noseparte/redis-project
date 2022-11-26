class Cache:

    def __init__(self, client):
        self.client = client

    def set(self, key, value):
        """
        把需要被缓存的数据存储到键key里面，如果键key已经有值，那么使用新值去覆盖旧值
        :param key:
        :param value:
        :return:
        """
        self.client.set(key, value)

    def get(self, key):
        """
        获取存储在键key里面的缓存数据，如果key不存在，那么返回None
        :param key:
        :return:
        """
        return self.client.get(key)

    def update(self, key, new_value):
        """
        对键key存储的缓存数据进行更新，并返回键key在被更新之前存储的缓存数据。
        如果键key之前并没有存储数据，那么返回None
        :param key:
        :param new_value:
        :return:
        """
        return self.client.getset(key, new_value)
