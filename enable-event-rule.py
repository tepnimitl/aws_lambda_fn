import json
import boto3

client = boto3.client('events')
rule_name = 'StartStop-Scheduler-SchedulerRule-4RHFF08EZN85'

def lambda_handler(event, context):
    # TODO implement
    
    response = client.enable_rule(
        Name = rule_name
    )
    status = client.describe_rule(
        Name = rule_name
        )
        
    status = status['State']
    print(rule_name +str(" : ") +str(status))
    
    return {
        'statusCode': 200,
        'rule_name': rule_name,
        'status': status,
        'body': json.dumps('Successfully!')
    }
