import boto3
import datetime

ec2_client = boto3.client('ec2')
ssm_client = boto3.client('ssm')

# Get all running EC2 instances
instances = ec2_client.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        
        try:
            # Check for active sessions
            sessions = ssm_client.describe_sessions(
                Filters=[
                    {
                        'key': 'Target',
                        'value': instance_id
                    }
                ],
                State='Active'
            )
            
            # If no active sessions, stop the instance
            if not sessions['Sessions']:
                print(f"No active sessions found for {instance_id}. Stopping instance...")
                # ec2_client.stop_instances(InstanceIds=[instance_id])
            else:
                print(f"Active session found for {instance_id}. Taking no action.")
                
        except Exception as e:
            print(f"Error processing instance {instance_id}: {str(e)}")
            continue
