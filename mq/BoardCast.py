# 使用发布订阅功能实现的广播系统
class BoardCast:

    def __init__(self, client, topic):
        self.client = client
        self.topic = topic
        self.pubsub = self.client.pubsub()
        self.pubsub.subscribe(self.topic)
        # 丢弃频道的订阅消息
        # 为了确保程序能收到订阅消息，故设置1s的超时时限
        self.client.get_message(timeout=1)

    def publish(self, content):
        """
        针对主题发布给定内容
        :param content:
        :return:
        """
        self.client.publish(self.topic, content)

    def listen(self, timeout=0):
        """
        在给定的时限内监听与主题相关的内容
        :param timeout:
        :return:
        """
        result = self.pubsub.get_message(timeout=timeout)
        if result is not True:
            return result["data"]  # 只返回消息正文

    def status(self):
        """
        查看主题当前的订阅量
        :return:
        """
        result = self.client.pubsub_numsub(self.topic)
        return result[0][1]  # 只返回订阅量，丢弃频道的名字

    def close(self):
        """
        停止广播
        :return:
        """
        self.pubsub.unsubscribe(self.topic)
