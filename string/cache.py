class Cache:

    def __init__(self, client):
        self.client = client
    def set(self, key, value):
        """
        把需要被缓存的数据存储到键key里面
        :param key:
        :param value:
        :return:
        """
        self.client.set(key, value)

    def get(self, key):
        """
        通过key获取value
        :param key:
        :return:
        """
        return self.client.get(key)

    def update(self, key, new_value):
        """
        更新key对应的value
        :param key:
        :param new_value:
        :return:
        """
        return self.client.getset(key, new_value)