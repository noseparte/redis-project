VALUE_OF_LOCK = "locking"

class Lock:
    def __init__(self, client, key):
        self.client = client
        self.key = key

    def acquire(self):
        """
        尝试获取锁。成功时返回TRUE，失败时返回FALSE
        :return:
        """
        result = self.client.set(self.key, VALUE_OF_LOCK, nx = True)
        return result is True

    def resease(self):
        """
        尝试释放锁。成功时返回TRUE，失败时返回FALSE
        :return:
        """
        return self.client.delete(self.key) == 1