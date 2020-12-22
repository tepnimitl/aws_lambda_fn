import json
import boto3

client = boto3.client('events')
sns = boto3.client('sns')
rule_name = 'StartStop-Scheduler-SchedulerRule-xxx'
sns_arn = 'arn:aws:sns:us-east-1:xxx:event-scheduler-status'

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
    
    response = sns.publish(
        TargetArn = sns_arn,
        Subject = 'xxx Scheduler Status',
        Message = 'xxx Scheduler Status : ' + status
    )
    
    return {
        'statusCode': 200,
        'rule_name': rule_name,
        'status': status,
        'body': json.dumps('Successfully!')
    }
