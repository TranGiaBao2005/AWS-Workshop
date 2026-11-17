import boto3
import logging

logging.basicConfig(level=logging.INFO)
# Khởi tạo ElastiCache client với Region us-east-1
client = boto3.client('elasticache', region_name='us-east-1')

def create_cluster_mode_enabled_rbac(
    CacheNodeType='cache.t4g.micro',
    EngineVersion='6.2',
    NumNodeGroups=2,
    ReplicasPerNodeGroup=1,
    ReplicationGroupDescription='Sample cache with cluster mode enabled and RBAC',
    ReplicationGroupId=None,
    UserGroupIds=None,
    SecurityGroupIds=None,
    CacheSubnetGroupName='subnet-group',
    CacheParameterGroupName='default.redis6.x.cluster.on'
):
    """Creates an Elasticache Cluster with cluster mode enabled and RBAC

    Returns a dictionary with the API response

    :param CacheNodeType: Node type used on the cluster.
    :param EngineVersion: Engine version to be used.
    :param NumNodeGroups: Number of shards in the cluster.
    :param ReplicasPerNodeGroup: Number of replicas per shard.
    :param ReplicationGroupDescription: Description for the cluster.
    :param ReplicationGroupId: Name for the cluster.
    :param UserGroupIds: List of user groups to be assigned to the cluster.
    :param SecurityGroupIds: List of security groups.
    :param CacheSubnetGroupName: Subnet group name.
    :param CacheParameterGroupName: Parameter group name.
    :return: dictionary with the API results
    """
    if not ReplicationGroupId:
        return 'ReplicationGroupId parameter is required'
    elif not isinstance(UserGroupIds, list):
        return {'Error': 'UserGroupIds parameter is required and must be a list'}

    params = {
        'AutomaticFailoverEnabled': True,
        'CacheNodeType': CacheNodeType,
        'Engine': 'redis',
        'EngineVersion': EngineVersion,
        'ReplicationGroupDescription': ReplicationGroupDescription,
        'ReplicationGroupId': ReplicationGroupId,
        'SnapshotRetentionLimit': 1,
        'TransitEncryptionEnabled': True,
        'UserGroupIds': UserGroupIds,
        'NumNodeGroups': NumNodeGroups,
        'ReplicasPerNodeGroup': ReplicasPerNodeGroup,
        'CacheParameterGroupName': CacheParameterGroupName
    }

    if isinstance(SecurityGroupIds, list):
        params.update({'SecurityGroupIds': SecurityGroupIds})
    if CacheSubnetGroupName:
        params.update({'CacheSubnetGroupName': CacheSubnetGroupName})

    response = client.create_replication_group(**params)
    return response


if __name__ == '__main__':
    # Khởi tạo cụm Cluster Mode Enabled có bật TLS và phân quyền RBAC
    response = create_cluster_mode_enabled_rbac(
        CacheNodeType='cache.t4g.micro',
        EngineVersion='6.2',
        ReplicationGroupDescription='Redis cluster mode enabled with RBAC and TLS SDK',
        ReplicationGroupId='redis-enabled-rbac-sdk',
        NumNodeGroups=2,
        ReplicasPerNodeGroup=1,
        UserGroupIds=[
            'mygroup'
        ],
        SecurityGroupIds=[
            'sg-06c03603fe1cca808'
        ],
        CacheSubnetGroupName='subnet-group',
        CacheParameterGroupName='default.redis6.x.cluster.on'
    )
    
    logging.info(response)
