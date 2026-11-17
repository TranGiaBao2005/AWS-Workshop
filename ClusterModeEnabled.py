import boto3
import logging

logging.basicConfig(level=logging.INFO)
# Khởi tạo ElastiCache client với Region us-east-1
client = boto3.client('elasticache', region_name='us-east-1')

def create_cluster_mode_enabled(
    CacheNodeType='cache.t4g.micro',
    EngineVersion='6.2',
    NumNodeGroups=2,
    ReplicasPerNodeGroup=1,
    ReplicationGroupDescription='Sample cache with cluster mode enabled',
    ReplicationGroupId=None,
    CacheSubnetGroupName='subnet-group',
    CacheParameterGroupName='default.redis6.x.cluster.on'
):
    """Creates an Elasticache Cluster with cluster mode enabled

    Returns a dictionary with the API response

    :param CacheNodeType: Node type used on the cluster.
    :param EngineVersion: Engine version to be used.
    :param NumNodeGroups: Number of shards in the cluster.
    :param ReplicasPerNodeGroup: Number of replicas per shard.
    :param ReplicationGroupDescription: Description for the cluster.
    :param ReplicationGroupId: Name for the cluster
    :param CacheSubnetGroupName: Subnet group for the cluster
    :param CacheParameterGroupName: Parameter group (default.redis6.x.cluster.on)
    :return: dictionary with the API results
    """
    if not ReplicationGroupId:
        return 'ReplicationGroupId parameter is required'
    
    response = client.create_replication_group(
        AutomaticFailoverEnabled=True,
        CacheNodeType=CacheNodeType,
        Engine='redis',
        EngineVersion=EngineVersion,
        ReplicationGroupDescription=ReplicationGroupDescription,
        ReplicationGroupId=ReplicationGroupId,
        NumNodeGroups=NumNodeGroups,
        ReplicasPerNodeGroup=ReplicasPerNodeGroup,
        CacheSubnetGroupName=CacheSubnetGroupName,
        CacheParameterGroupName=CacheParameterGroupName,
        SnapshotRetentionLimit=1
    )

    return response


if __name__ == '__main__':
    # Khởi tạo cụm Cluster Mode Enabled (2 Shards, 1 Replica/Shard)
    response = create_cluster_mode_enabled(
        CacheNodeType='cache.t4g.micro',
        EngineVersion='6.2',
        ReplicationGroupDescription='Redis cluster mode enabled with replicas SDK',
        ReplicationGroupId='redis-enabled-sdk',
        NumNodeGroups=2,
        ReplicasPerNodeGroup=1,
        CacheSubnetGroupName='subnet-group',
        CacheParameterGroupName='default.redis6.x.cluster.on'
    )

    logging.info(response)
