#coding=utf-8

# 使用有序集合实现的排行榜程序
class RankingList:

    def __init__(self, client, key):
        self.client = client
        self.key = key

    def set_score(self, item, score):
        """
        为排行榜中的指定元素设置分数，不存在的元素会被添加到排行榜中
        :param item:
        :param score:
        :return:
        """
        self.client.sadd(self.key, {item:score})

    def get_score(self, item):
        """

        :param item:
        :return:
        """
        return self.client.zscore(self.key, item)

    def remove(self, item):
        """

        :param item:
        :return:
        """
        self.client.zrem(self.key, item)

    def increase_score(self, item, increment):
        """

        :param item:
        :param increment:
        :return:
        """
        self.client.zincrby(self.key, increment, item)

    def decrease_score(self, item, decrement):
        """

        :param item:
        :param decrement:
        :return:
        """
        self.client.zincrby(self.key, 0-decrement, item)

    def get_rank(self, item):
        """

        :param item:
        :return:
        """
        rank = self.client.zrevrank(self.key, item)
        if rank is not None:
            return rank + 1;

    def top(self, n, with_score=False):
        """

        :param n:
        :param with_score:
        :return:
        """
        return self.client.zrevrange(self.key, 0 , n-1, withscores=with_score)