#coding:utf-8

import unittest

from redis import Redis

from strings.cache import Cache


class TestVote(unittest.TestCase):

    def setUp(self):
        self.client = Redis("192.168.1.5", 6379, 1)
        self.client.flushdb()

        self.cache = Cache(self.client)

    def test_set(self):
        self.cache.set("name", "noseparte")

    def test_get(self):
        return self.client.get("name")

    def test_update(self):
        return self.client.getset("name", "haoyitao")

