import boto3
import logging

logging.basicConfig(level=logging.INFO)
# Khởi tạo ElastiCache client với Region us-east-1 (Bắc Virginia)
client = boto3.client('elasticache', region_name='us-east-1')

def create_cluster_mode_disabled(
    CacheNodeType='cache.t4g.micro',
    EngineVersion='6.0',
    NumCacheClusters=2,
    ReplicationGroupDescription='Sample cache cluster',
    ReplicationGroupId=None,
    CacheSubnetGroupName='subnet-group'
):
    """Creates an Elasticache Cluster with cluster mode disabled

    Returns a dictionary with the API response

    :param CacheNodeType: Node type used on the cluster. Default: cache.t4g.micro
    :param EngineVersion: Engine version to be used. Default: 6.0
    :param NumCacheClusters: Number of nodes in the cluster (1 primary + replicas)
    :param ReplicationGroupDescription: Description for the cluster.
    :param ReplicationGroupId: Name for the cluster
    :param CacheSubnetGroupName: Tên Subnet Group (subnet-group)
    :return: dictionary with the API results
    """
    if not ReplicationGroupId:
        return 'ReplicationGroupId parameter is required'

    response = client.create_replication_group(
        AutomaticFailoverEnabled=True,
        CacheNodeType=CacheNodeType,
        Engine='redis',
        EngineVersion=EngineVersion,
        NumCacheClusters=NumCacheClusters,
        ReplicationGroupDescription=ReplicationGroupDescription,
        ReplicationGroupId=ReplicationGroupId,
        CacheSubnetGroupName=CacheSubnetGroupName,
        SnapshotRetentionLimit=1,
    )
    return response


if __name__ == '__main__':
    # Khởi tạo cụm ElastiCache Cluster Mode Disabled bằng Boto3 SDK
    elasticacheResponse = create_cluster_mode_disabled(
        CacheNodeType='cache.t4g.micro',
        EngineVersion='6.0',
        NumCacheClusters=2,
        ReplicationGroupDescription='Redis cluster mode disabled with replicas',
        ReplicationGroupId='redis-disabled-sdk',
        CacheSubnetGroupName='subnet-group'
    )
    
    logging.info(elasticacheResponse)
