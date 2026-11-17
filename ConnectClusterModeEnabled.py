import logging

logging.basicConfig(level=logging.INFO)

# Configuration Endpoint của cụm Cluster Mode Enabled (my-cluster-enable)
# Lưu ý: Cụm này nằm trong Private Subnet của VPC, kết nối chuẩn từ EC2 cùng VPC
HOST = "my-cluster-enable.1vblox.clustercfg.use1.cache.amazonaws.com"
PORT = 6379

# Hỗ trợ cả thư viện redis mới (redis >= 4.0/5.0/8.0) và rediscluster cũ
try:
    from redis.cluster import RedisCluster
    redis = RedisCluster(
        host=HOST,
        port=PORT,
        decode_responses=True,
        socket_timeout=5
    )
except ImportError:
    from rediscluster import RedisCluster
    redis = RedisCluster(
        startup_nodes=[{"host": HOST, "port": str(PORT)}],
        decode_responses=True,
        skip_full_coverage_check=True
    )

try:
    if redis.ping():
        logging.info("Connected to Redis Cluster (Mode Enabled) successfully!")
except Exception as e:
    logging.error(f"Lỗi kết nối tới Redis Cluster: {e}")
