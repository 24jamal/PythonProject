import boto3
from lambda_handler import lambda_handler

def simulate_lambda(queue_url):

    sqs = boto3.client("sqs", region_name="us-east-1")

    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10
    )

    records = []

    for msg in response.get("Messages", []):

        records.append({
            "messageId": msg["MessageId"],
            "body": msg["Body"]
        })

    event = {"Records": records}

    lambda_handler(event, None)