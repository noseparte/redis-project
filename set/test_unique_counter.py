import unittest

from redis import Redis

from set.unique_counter import UniqueCounter


class TestUniqueCounter(unittest.TestCase):

    def setUp(self):
        self.client = Redis("192.168.1.5", 6379, 1)
        self.client.flushdb()

        self.counter = UniqueCounter(self.client, "test-counter")

    def test_count_in(self):
        self.assertEqual(
            self.counter.get_result(),
            0
        )

        self.counter.count_in("a")

        self.assertNotEqual(
            self.counter.get_result(),
            0
        )

    def test_get_result(self):
        self.assertEqual(
            self.counter.get_result(),
            0
        )

        self.counter.count_in("a")

        self.assertEqual(
            self.counter.get_result(),
            1
        )

    def test_counter_will_not_count_twice(self):
        self.counter.count_in("a")
        self.counter.count_in("a")
        self.assertEqual(
            self.counter.get_result(),
            1
        )


if __name__ == '__main__':
    unittest.main()
