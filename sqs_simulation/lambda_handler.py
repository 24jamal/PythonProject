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

        order_id = body["order_id"]
        amount = body["amount"]

        if is_duplicate(message_id):
            print("Duplicate skipped")
            continue

        try:

            if amount == 500:
                raise Exception("Simulated failure")

            cursor.execute(
                "INSERT INTO orders(order_id, amount, status) VALUES (%s,%s,%s)",
                (order_id, amount, "processed")
            )

            print(f"Order processed {order_id}")

        except Exception as e:

            print("Error:", e)

            failures.append({
                "itemIdentifier": message_id
            })

    return {
        "batchItemFailures": failures
    }