* 导入模块  

``` python
import redis
```

* 文件内容  

    [Redis.py](../pythonFile/Redis.py)

* 主要方法  

``` python
config_redis = dict(
    host='192.168.0.179',
    port=6379,
    db=0,
    password='123456',
    decode_responses=True
)

# 生成连接池对象
pool = redis.ConnectionPool(**config_redis)
# 创建连接
conn = redis.StrictRedis(connection_pool=pool)
# 设置key:value
conn.set('name', 'zhangsan')
# 读取key内容
print(conn.get('name'))
# 关闭连接
conn.close()
```
