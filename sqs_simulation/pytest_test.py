import boto3
from moto import mock_aws

from producer import send_messages
from consumer_simulator import process_batch

@mock_aws
def test_pipeline():

    sqs = boto3.client("sqs", region_name="us-east-1")

    queue = sqs.create_queue(
        QueueName="orders-queue"
    )

    queue_url = queue["QueueUrl"]

    send_messages(queue_url)

    process_batch(queue_url)