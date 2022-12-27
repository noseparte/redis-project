# coding=utf-8
"""
#author noseparte
#link noseparte@github.com
#create 2022/12/27 - 20:44
#description 倒计时式的限速器
"""


class Limiter:

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def set_max_execute(self, max_execute_times):
        """
        设置操作的最大可执行数
        :param max_execute_times:
        :return:
        """
        self.client.set(self.key, max_execute_times)

    def still_vaild_to_execute(self):
        """
        检查是否可以继续执行被限制的操作，是则返回TRUE，否则返回FALSE
        :return:
        """
        num = self.client.decr(self.key)
        return num >= 0

    def remaining_execute(self):
        """
        返回操作的剩余可执行次数
        :return:
        """
        num = int(self.client.get(self.key))
        if num < 0:
            return 0
        else:
            return num
