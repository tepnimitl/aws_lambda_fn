import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    
    instance_id = event['detail']['instance-id']
    print("Instance-Id: " + instance_id)
    
    state = event['detail']['state']
    print("State: " + state)
    
    response = ec2.describe_tags(
        Filters=[
            {
                'Name': 'resource-id',
                'Values': [instance_id]
            }
        ]
    )
    
    key = response['Tags']
    for tags in key:
        if tags['Key'] == 'Name':
            server_name = tags['Value']
            print("Server Name: " + server_name)
            
    
    """ # Condition if an instance is down, will bring another instance
    if state == 'stopped':
        print(state)
        ec2.start_instances(InstanceIds = ['i-0dff65abe046273d3'])
    elif state == 'running':
        print(state)
    """    
    
    return {
        'instance_id': instance_id,
        'state': state,
        'server_name': server_name,
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
