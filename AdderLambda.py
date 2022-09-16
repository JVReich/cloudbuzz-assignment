import json
import boto3

def lambda_handler(event, context):
    num1 = event['num1']
    num2 = event['num2']
    if num1.isnumeric() and num2.isnumeric():
        sum = int(num1)+int(num2)
        sns = boto3.client('sns')
        response = sns.publish(
            TopicArn = 'arn:aws:sns:us-east-1:810622864182:AdderTopic',
            Message = 'The sum of the two given numbers is: ' + str(sum),
            )
        return sum
    else:
        err1 = "Only numbers can serve as input"
        return err1