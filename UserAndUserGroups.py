import boto3
import logging

logging.basicConfig(level=logging.INFO)
# Khởi tạo ElastiCache client với Region us-east-1
client = boto3.client('elasticache', region_name='us-east-1')

def check_user_exists(UserId):
    """Kiểm tra UserId đã tồn tại trên ElastiCache chưa"""
    try:
        response = client.describe_users(UserId=UserId)
        if response['Users'][0]['UserId'].lower() == UserId.lower():
            return True
    except Exception as e:
        if hasattr(e, 'response') and e.response['Error']['Code'] == 'UserNotFound':
            logging.info(f"User {UserId} chưa tồn tại.")
            return False
        else:
            return False

def check_group_exists(UserGroupId):
    """Kiểm tra UserGroupId đã tồn tại trên ElastiCache chưa"""
    try:
        response = client.describe_user_groups(UserGroupId=UserGroupId)
        if response['UserGroups'][0]['UserGroupId'].lower() == UserGroupId.lower():
            return True
    except Exception as e:
        if hasattr(e, 'response') and e.response['Error']['Code'] == 'UserGroupNotFound':
            logging.info(f"UserGroup {UserGroupId} chưa tồn tại.")
            return False
        else:
            return False

def create_user(UserId=None, UserName=None, Password=None, AccessString=None):
    """Tạo người dùng mới trong ElastiCache"""
    try:
        response = client.create_user(
            UserId=UserId,
            UserName=UserName,
            Engine='Redis',
            Passwords=[Password],
            AccessString=AccessString,
            NoPasswordRequired=False
        )
        return response['ARN']
    except Exception as e:
        logging.error(f"Lỗi tạo user {UserId}: {e}")
        return str(e)

def create_group(UserGroupId=None, UserIds=None):
    """Tạo nhóm người dùng (User Group) RBAC mới"""
    try:
        response = client.create_user_group(
            UserGroupId=UserGroupId,
            Engine='Redis',
            UserIds=UserIds
        )
        return response['ARN']
    except Exception as e:
        logging.error(f"Lỗi tạo group {UserGroupId}: {e}")
        return str(e)


if __name__ == '__main__':
    # Tạo đồng thời cả 'mygroup' (cho bài 4.1.1/4.1.2) và 'mygroup2' (cho bài 4.1.3)
    target_groups = ['mygroup', 'mygroup2']
    
    for groupName in target_groups:
        userName = 'myuser' if groupName == 'mygroup' else 'myuser2'
        userId = groupName + '-' + userName

        # 1. Tạo user chính và user 'default' (Bắt buộc phải có user 'default' trong nhóm RBAC)
        for tmpUserId, tmpUserName in [(userId, userName), (groupName + '-default', 'default')]:
            if not check_user_exists(tmpUserId):
                logging.info(f"Đang tạo người dùng: {tmpUserId} (UserName: {tmpUserName})")
                response = create_user(
                    UserId=tmpUserId,
                    UserName=tmpUserName,
                    Password='MyStrongPasswordWithNumbers123',
                    AccessString='on ~* +@all'
                )
                logging.info(f"Tạo user thành công: {response}")
            else:
                logging.info(f"User {tmpUserId} đã tồn tại.")

        # 2. Tạo User Group và liên kết các UserIds vào nhóm
        if not check_group_exists(groupName):
            logging.info(f"Đang tạo User Group: {groupName}")
            UserIds = [userId, groupName + '-default']
            response = create_group(UserGroupId=groupName, UserIds=UserIds)
            logging.info(f"Tạo User Group {groupName} thành công: {response}")
        else:
            logging.info(f"User Group {groupName} đã tồn tại.")
