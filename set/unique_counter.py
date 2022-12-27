# coding=utf-8
"""
#author noseparte
#link noseparte@github.com
#create 2022/12/27 - 20:50
#description 唯一计数器
"""


class UniqueCounter:

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def count_in(self, item):
        """
        尝试将给定元素计入计数器当中
        如果给定元素之前沒有被计数过，那么方法返回TRUE表示此次计数有效
        如果给定元素之前已经被技术过，那么方法返回FALSE表示此次计数无效
        :param item:
        :return:
        """
        return self.client.sadd(self.key, item) == 1

    def get_result(self):
        """
        返回计数器的值
        :return:
        """
        return self.client.scard(self.key)
