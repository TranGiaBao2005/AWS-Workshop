import boto3
import logging

logging.basicConfig(level=logging.INFO)
# Khởi tạo ElastiCache client với Region us-east-1
client = boto3.client('elasticache', region_name='us-east-1')

def create_cluster_mode_disabled_rbac(
    CacheNodeType='cache.t4g.micro',
    EngineVersion='6.0',
    NumCacheClusters=2,
    ReplicationGroupDescription='Sample cache cluster',
    ReplicationGroupId=None,
    UserGroupIds=None,
    SecurityGroupIds=None,
    CacheSubnetGroupName=None
):
    """Creates an Elasticache Cluster with cluster mode disabled and RBAC

    Returns a dictionary with the API response

    :param CacheNodeType: Node type used on the cluster.
    :param EngineVersion: Engine version to be used.
    :param NumCacheClusters: Number of nodes in the cluster.
    :param ReplicationGroupDescription: Description for the cluster.
    :param ReplicationGroupId: Mandatory name for the cluster.
    :param UserGroupIds: Mandatory list of user groups to be assigned to the cluster.
    :param SecurityGroupIds: List of security groups to be assigned.
    :param CacheSubnetGroupName: Subnet group where the cluster will be placed.
    :return: dictionary with the API results
    """
    if not ReplicationGroupId:
        return {'Error': 'ReplicationGroupId parameter is required'}
    elif not isinstance(UserGroupIds, list):
        return {'Error': 'UserGroupIds parameter is required and must be a list'}

    params = {
        'AutomaticFailoverEnabled': True,
        'CacheNodeType': CacheNodeType,
        'Engine': 'redis',
        'EngineVersion': EngineVersion,
        'NumCacheClusters': NumCacheClusters,
        'ReplicationGroupDescription': ReplicationGroupDescription,
        'ReplicationGroupId': ReplicationGroupId,
        'SnapshotRetentionLimit': 1,
        'TransitEncryptionEnabled': True,
        'UserGroupIds': UserGroupIds
    }

    # defaults will be used if CacheSubnetGroupName or SecurityGroups are not explicit.
    if isinstance(SecurityGroupIds, list):
        params.update({'SecurityGroupIds': SecurityGroupIds})
    if CacheSubnetGroupName:
        params.update({'CacheSubnetGroupName': CacheSubnetGroupName})

    response = client.create_replication_group(**params)
    return response


if __name__ == '__main__':
    # Khởi tạo cụm ElastiCache với mã hóa TLS và xác thực nhóm quyền RBAC (UserGroupIds)
    response = create_cluster_mode_disabled_rbac(
        CacheNodeType='cache.t4g.micro',
        EngineVersion='6.0',
        NumCacheClusters=2,
        ReplicationGroupDescription='Redis cluster mode disabled with RBAC',
        ReplicationGroupId='redis-rbac-sdk',
        UserGroupIds=[
            'mygroup'
        ],
        SecurityGroupIds=[
            'sg-06c03603fe1cca808'
        ],
        CacheSubnetGroupName='subnet-group'
    )

    logging.info(response)
