from redis import Redis
import logging

logging.basicConfig(level=logging.INFO)

# Cấu hình thông số kết nối tới cụm ElastiCache Redis (chế độ Disabled có TLS & RBAC)
# Host là Primary Endpoint của cụm redis-rbac-sdk
HOST = 'master.redis-rbac-sdk.1vblox.use1.cache.amazonaws.com'
PORT = 6379
USERNAME = 'myuser'
PASSWORD = 'MyStrongPasswordWithNumbers123'

# Khởi tạo đối tượng kết nối Redis với TLS (ssl=True) và xác thực tài khoản RBAC
redis = Redis(
    host=HOST,
    port=PORT,
    decode_responses=True,
    ssl=True,
    username=USERNAME,
    password=PASSWORD,
    socket_timeout=5
)

try:
    if redis.ping():
        logging.info("Connected to Redis successfully!")
except Exception as e:
    logging.error(f"Lỗi kết nối tới Redis: {e}")
