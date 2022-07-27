import boto3

ec2 = boto3.client('ec2')

class Instance(object):
    def __init__(self) -> None:
        pass

    def listInstance():
        list = ec2.describe_instances()
        return list

    def startInstance(self, instanceId):
        ec2.start_instances(InstanceIds=[instanceId])
    
    def stopInstance(self, instanceId):
        ec2.stop_instances(InstanceIds=[instanceId])

