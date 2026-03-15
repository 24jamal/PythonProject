import boto3
import json

def send_messages(queue_url):

    sqs = boto3.client("sqs", region_name="us-east-1")

    for i in range(10):

        body = {
            "order_id": i+1,
            "amount": (i+1)*100
        }

        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(body)
        )