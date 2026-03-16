import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def is_duplicate(message_id):

    key = f"fdr:{message_id}"

    if redis_client.exists(key):
        return True

    redis_client.set(key, "processed", ex=3600)

    return False