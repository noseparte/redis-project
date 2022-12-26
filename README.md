## 项目简介

项目内容分为俩部分: 
- **Redis使用手册** 
- **Redis5设计与源码分析**

## Redis数据结构

### 字符串(string)
- [示例: 缓存](strings/cache.py)
- [示例: 锁](strings/lock.py)
- [示例: 存储文章信息](strings/article.py)
- [示例: 使用字符串键实现高效的日志存储程序](strings/log.py)

### 哈希(hash)
- [示例: 使用散列实现的短网址程序](hash/shorty_url.py)

### 列表(list)
- [示例: 使用列表实现的先进先出队列](list/fifo_queue.py)

### 集合(set)
- [示例：投票](set/vote.py)

### 有序集合(zset)
- [示例: 使用有序集合实现的排行榜程序](zset/ranking_list.py)
