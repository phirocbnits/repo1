import boto3
from botocore.exceptions import ClientError
#from dotenv import load_dotenv
#import os

#load_dotenv()
#security=os.getenv('security_name')


def createSecurityGroup(security,desc = "ph_sg"):
    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs()
    #to get the default vpc_id
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

    try:
        response = ec2.create_security_group(GroupName=security,
                                            Description=desc,
                                            VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group: %s in vpc %s.' % (security_group_id, vpc_id))

        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])
        print('Ingress Successfully Set %s' % data)
        return security_group_id
    except ClientError as e:
        print(e)

