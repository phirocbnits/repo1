import boto3
from botocore.exceptions import ClientError 
ec2 = boto3.client("ec2")
#to view instances
#print(ec2.describe_instances())

def createKeyPair(keyname):
    try:
        key = ec2.create_key_pair(KeyName = keyname)
        filename = keyname + ".pem"
        print(key)
        with open(filename,"w") as file1:
            file1.write(key['KeyMaterial'])
            file1.close
        print("key created")
    except ClientError as e:
        print(e)

