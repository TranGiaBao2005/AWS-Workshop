import time
import logging
from redis.cluster import RedisCluster

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')

# Khởi tạo kết nối tới cụm Redis Cluster Mode Enabled (my-cluster-enable)
redis = RedisCluster(
    host="my-cluster-enable.1vblox.clustercfg.use1.cache.amazonaws.com",
    port=6379,
    decode_responses=True
)

keyName = 'mykey'
currTime = time.ctime(time.time())

# Set key 'mykey' với giá trị thời gian hiện tại.
# Key sẽ tự động hết hạn và xóa khỏi cache sau 60 giây (ex=60).
redis.set(keyName, currTime, ex=60)

# Tạm dừng 5 giây để minh họa giá trị TTL (Time To Live) giảm dần
time.sleep(5)

# Lấy giá trị của key và thời gian hết hạn TTL hiện tại
keyValue = redis.get(keyName)
keyTTL = redis.ttl(keyName)

logging.info("Key {} was set at {} and has {} seconds until expired".format(keyName, keyValue, keyTTL))
