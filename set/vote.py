def vote_up_key(vote_target):
    return vote_target + "::vote_up"

def vote_down_key(vote_target):
    return vote_target + "::vote_down"

class Vote:
    def __init__(self, client, vote_target):
        self.client = client
        self.vote_up_set = vote_up_key(vote_target)
        self.vote_down_set = vote_down_key(vote_target)

    def is_voted(self, user):
        """
        检查用户是否已经投过票
        :param user:
        :return:
        """
        return self.client.sismember(self.vote_up_set, user) or \
            self.client.sismember(self.vote_down_set, user)

    def vote_up(self, user):
        """
        让用户投赞成票
        :param user:
        :return:
        """
        if self.is_voted(user):
            return False
        self.client.sadd(self.vote_up_set, user)
        return True

    def vote_down(self, user):
        """
        让用户投反对票
        :param user:
        :return:
        """
        if self.is_voted(user):
            return False
        self.client.sadd(self.vote_down_set, user)

    def undo(self, user):
        """
        取消用户的投票
        :param user:
        :return:
        """
        self.client.srem(self.vote_up_set, user)
        self.client.srem(self.vote_down_set, user)

    def vote_up_count(self):
        """
        返回投支持票的用户数量
        :return:
        """
        return self.client.scard(self.vote_up_set)

    def get_all_vote_up_users(self):
        """
        返回所有投支持票的用户
        :return:
        """
        return self.client.smembers(self.vote_up_set)

    def vote_down_count(self):
        """
        返回投反对票的用户数量
        :return:
        """
        return self.client.scard(self.vote_down_set)

    def get_all_vote_down_users(self):
        """
        返回投反对票的所有用户
        :return:
        """
        return self.client.smembers(self.vote_down_set)