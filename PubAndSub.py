import logging
import time
from redis import Redis

def handlerFunction(message):
    """Prints message got from PubSub channel to the log output

    Return None
    :param message: message to log
    """
    logging.info(message)

logging.basicConfig(level=logging.INFO)

# Sử dụng Primary Endpoint của cụm Redis Cluster Mode Disabled (my-cluster-disable)
redis = Redis(
    host="my-cluster-disable.1vblox.ng.0001.use1.cache.amazonaws.com",
    port=6379,
    decode_responses=True
)

# Tạo kết nối subscriber lắng nghe trên channel "mychannel"
subscriber = redis.pubsub()
subscriber.subscribe(**{'mychannel': handlerFunction})

# Chạy subscriber trong một thread riêng biệt để lắng nghe tin nhắn trong khi luồng chính tiếp tục chạy
thread = subscriber.run_in_thread(sleep_time=0.01)

# Gửi tin nhắn đầu tiên trên channel "mychannel"
redis.publish('mychannel', 'My message')

# Liên tục publish tin nhắn thời gian hiện tại mỗi giây.
# Subscriber thread ở chế độ ngầm sẽ bắt tin nhắn và in ra màn hình.
# Nhấn Ctrl + C trong terminal để dừng chương trình.
try:
    while True:
        redis.publish('mychannel', time.ctime(time.time()))
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Đã nhận tín hiệu dừng. Đang tắt PubSub...")
    thread.stop()
