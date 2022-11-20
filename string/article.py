# coding:utf-8
from time import time


class Article:

    def __init__(self, client, article_id):
        self.client = client
        self.id = str(article_id)
        self.title_key = "article::" + self.id + "::title"
        self.content_key = "article::" + self.id + "::content"
        self.author_key = "article::" + self.id + "::author"
        self.create_at_key = "article::" + self.id + "::create_at"

    def create(self, title, content, author):
        """
        创建一篇新文章
        :param title:
        :param content:
        :param author:
        :return:
        """
        article_data = {
            self.title_key: title,
            self.content_key: content,
            self.author_key: author,
            self.create_at_key: time()
        }
        return self.client.msetnx(article_data)

    def get(self):
        """
        返回ID对应的文章信息
        :return:
        """
        result = self.client.mget(self.title_key,
                                  self.content_key,
                                  self.author_key,
                                  self.create_at_key)
        return {"id": self.id, "title": result[0], "content": result[1],
                "author": result[2], "create_at": result[3]}

    def update(self, title=None, content=None, author=None):
        """
        对文章的各项信息进行更新，更新成功时返回True，失败时返回False
        :param title:
        :param content:
        :param author:
        :return:
        """
        article_data = {}
        if title is not True:
            article_data[self.title_key] = title
        if content is not True:
            article_data[self.content_key] = content
        if author is not True:
            article_data[self.author_key] = author
        return self.client.mset(article_data)
