import boto3

def lambda_handler(event, context):
    ebs =  boto3.client('ec2')
    response = ebs.describe_volumes(Filters=[{'Name': 'status','Values': ['available']}])
    for volumes in response['Volumes']:
        volume_id = volumes.get('VolumeId')
        if volumes['State'] == 'available':
            response = ebs.delete_volume(
                VolumeId=volume_id
            )

#Remember to adjust function execution time above 3 secs of it won't work.
