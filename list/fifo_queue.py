#conding=utf-8

# 使用列表实现的先进先出队列
class FIFOqueue:

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def enqueue(self, item):
        """
        将给定元素放入队列，然后返回队列当前包含的元素数量作为结果
        :param item:
        :return:
        """
        return self.client.rpush(self.key, item)

    def dequeue(self):
        """
        移除并返回队列中目前入队时间最长的元素
        :return:
        """
        return self.client.lpop(self.key)