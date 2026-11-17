import logging
import time
from redis.cluster import RedisCluster

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')

# Khởi tạo kết nối tới cụm Redis Cluster Mode Enabled (my-cluster-enable)
redis = RedisCluster(
    host="my-cluster-enable.1vblox.clustercfg.use1.cache.amazonaws.com",
    port=6379,
    decode_responses=True
)

keyName = 'mykey'
# Xóa key cũ nếu còn tồn tại từ bài trước để tránh lỗi WRONGTYPE
redis.delete(keyName)

keyValues = {
    'datetime': time.ctime(time.time()),
    'epochtime': str(time.time())
}

# Ghi cấu trúc Hash 'myhash' với nhiều trường (datetime và epochtime)
redis.hset(keyName, mapping=keyValues)

# Đặt thời gian sống hết hạn cho key là 60 giây
redis.expire(keyName, 60)

# Tạm dừng 5 giây để minh họa giá trị TTL giảm dần
time.sleep(5)

# Lấy toàn bộ các trường trong Hash và thời gian TTL còn lại
resultValues = redis.hgetall(keyName)
keyTTL = redis.ttl(keyName)

logging.info("Key {} was set at {} and has {} seconds until expired".format(keyName, resultValues, keyTTL))
