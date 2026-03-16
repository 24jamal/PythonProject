import boto3
import json
from db import get_connection

sqs = boto3.client("sqs", region_name="us-east-1")

QUEUE_URL = "YOUR_SQS_URL"

def publish_fdr_transactions():

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
    SELECT * FROM merchant_fdr_transactions
    WHERE status='pending'
    """)

    rows = cursor.fetchall()

    for row in rows:

        sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(row)
        )

    print(f"{len(rows)} merchant FDR records sent to queue")