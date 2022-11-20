# 使用散列实现的短网址程序
from hash.base36 import base10_to_base36

ID_COUNTER = "ShortyUrl:id_counter"
URL_HASH = "ShortyUrl:url_hash"

class ShortyUrl:

    def __init__(self, client):
        self.client = client

    def shorten(self, target_url):
        """
        为目标网址创建并存储相应的短网址ID
        :param target_url:
        :return:
        """
        # 为目标网址创建新的数字ID
        new_id = self.client.incr(ID_COUNTER)
        # 通过将十进制数字转换为三十六进制数字来创建短网址ID
        # 比如，十进制数字10086将被转换为三十六进制数字7S6
        short_id = base10_to_base36(new_id)
        # 将短网址ID用作字段，目标网址用作值，将它们之间的映射关系存储到散列里面
        self.client.hset(URL_HASH, short_id, target_url)
        return short_id

    def restore(self, short_id):
        """
        根据给定的短网址ID，返回与之对应的目标网址
        :param short_id:
        :return:
        """
        return self.client.hget(URL_HASH, short_id)