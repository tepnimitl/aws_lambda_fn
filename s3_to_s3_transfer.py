# Trigger Lambda function when there is an upload file to bucket 's3temp002'
# file extension .txt will transfer to bucket 's3temp001' in directory txt/ and add prefix 'copy_'
# file extension .jpg will transfer to bucket 's3temp001' in directory jpg/ and add prefix 'copy_'
# The less will transfer to bucket 's3temp003' in directory junk/ with prefix 'unknown_'

import json
import boto3

s3 = boto3.resource('s3')
    

def lambda_handler(event, context):
    # TODO implement

    record = event['Records'][0]
    s_obj = record['s3']['object']['key']
    print("=====")
    print(event)
    print("=====")
    print(s_obj[-4:])
    
    copy_source = {
        'Bucket': 's3temp002',
        'Key': s_obj
    }
    
    if s_obj[-4:] == '.txt':
        bucket = s3.Bucket('s3temp001')
        d_obj = bucket.Object('txt/copy_' + s_obj)
        d_obj.copy(copy_source)
    elif s_obj[-4:] == '.jpg':
        bucket = s3.Bucket('s3temp001')
        d_obj = bucket.Object('jpg/copy_' + s_obj)
        d_obj.copy(copy_source)
    else:
        bucket = s3.Bucket('s3temp003')
        d_obj = bucket.Object('junk/unknown_' + s_obj)
        d_obj.copy(copy_source)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

