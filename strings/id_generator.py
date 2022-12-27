# coding=utf-8
"""
#author noseparte
#link noseparte@github.com
#create 2022/12/27 - 17:44
#description ID生成器
"""


class IdGenerator:

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def produce(self):
        """
        生成并返回下一个ID
        :return:
        """
        return self.client.incr(self.key)

    def reserve(self, n):
        """
        保留前n个ID，使得之后执行的produce()方法产生的ID都大于n。为了避免produce()方法产生重复ID。
        这个方法只能在produce()方法和reserve()方法都没有执行过的情况下使用。
        这个方法在ID被成功保留时返回TRUE，在produce()方法或reserve()方法已经执行过而导致保留失败时返回FALSE
        :param n:
        :return:
        """
        result = self.client.set(self.key, n, nx=True)
        return result is True
