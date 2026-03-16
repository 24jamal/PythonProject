import json
from db import get_connection
from redis_idempotency import is_duplicate

def lambda_handler(event, context):

    conn = get_connection()
    cursor = conn.cursor()

    failures = []

    for record in event["Records"]:

        message_id = record["messageId"]
        body = json.loads(record["body"])

        if is_duplicate(message_id):
            continue

        try:

            merchant_id = body["merchant_id"]
            terminal_id = body["terminal_id"]
            transaction_amount = body["transaction_amount"]

            print("Processing Merchant:", merchant_id)

            cursor.execute("""
            UPDATE merchant_fdr_transactions
            SET status='processed'
            WHERE id=%s
            """, (body["id"],))

        except Exception as e:

            print("Processing error:", e)

            failures.append({
                "itemIdentifier": message_id
            })

    return {
        "batchItemFailures": failures
    }