"""
#author noseparte
#link noseparte@github.com
#create 2022/12/27 - 17:43
#description 计数器
"""


class Counter:

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def increase(self, n=1):
        """
        将计数器的值加上n，然后返回计数器当前的值。
        如果用户没有显示地指定n，那么将计数器加上1
        :param n:
        :return:
        """
        return self.client.incr(self.key, n)

    def decrease(self, n=1):
        """
        将计数器的值减去n，然后返回计数器当前的值。
        如果用户没有显示地指定n，那么将计数器减去1
        :param n:
        :return:
        """
        return self.client.decr(self.key, n)

    def get(self):
        """
        返回计数器当前的值
        :return:
        """
        # 尝试获取计数器当前的值
        value = self.client.get(self.key)
        # 如果计数器并不存在，那么返回0作为计数器的默认值
        if value is None:
            return 0
        else:
            # 因为redis-py的get()方法返回的是字符串值，所以这里需要使用init()函数将
            # 字符串格式的数字转换为真正的数字类型，比如将"10"转换为10
            return int(value)

    def reset(self):
        """
        清零计数器，并返回计数器再被清零之前的值
        :return:
        """
        old_value = self.client.getset(self.key, 0)
        # 如果计数器之前并不存在，那么返回0作为它的旧值
        if old_value is None:
            return 0
        else:
            # 因为redis-py的get()方法一样，getset()方法返回的也是字符串值，所以程序在
            # 将计数器的旧值返回给调用者之前，需要先将它转换成真正的数字
            return int(old_value)