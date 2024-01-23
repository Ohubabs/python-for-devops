import boto3

def ebs_describe():
    ebs =  boto3.client('ec2')
    response = ebs.describe_volumes(Filters=[{'Name': 'status','Values': ['available']}])
    for volumes in response['Volumes']:
        volume_id = volumes.get('VolumeId')
        if volumes['State'] == 'available':
            response = ebs.delete_volume(
                VolumeId=volume_id
            )
    
ebs_describe()
