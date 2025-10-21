import time
from functools import wraps
from collections import deque
from threading import Lock

class RateLimitError(Exception):
    """Raised when a function exceeds its allowed call rate."""
    pass

def rate_limit(calls=3, per_seconds=5):
    """
    Decorator to limit how often a function can be called.
    Allows `calls` invocations per `per_seconds` time window.
    
    Usage:
        @rate_limit(calls=3, per_seconds=5)
        def api_call(): ...
    """
    if calls <= 0 or per_seconds <= 0:
        raise ValueError("calls and per_seconds must be positive")

    def decorator(func):
        timestamps = deque()   # when recent calls happened
        lock = Lock()          # thread-safety for check+record

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            with lock:
                # Drop timestamps outside the current window
                cutoff = now - per_seconds
                while timestamps and timestamps[0] <= cutoff:
                    timestamps.popleft()

                if len(timestamps) >= calls:
                    # Too many calls; compute wait time until next slot opens
                    oldest = timestamps[0]
                    wait = per_seconds - (now - oldest)
                    raise RateLimitError(
                        f"Rate limit exceeded: allowed {calls} calls per "
                        f"{per_seconds}s. Try again in {wait:.2f}s."
                    )

                # Record this call
                timestamps.append(now)

            # Execute the function outside the lock
            return func(*args, **kwargs)

        # Optional helpers for introspection/testing
        def remaining():
            with lock:
                now_local = time.time()
                # purge stale before counting
                cutoff_local = now_local - per_seconds
                while timestamps and timestamps[0] <= cutoff_local:
                    timestamps.popleft()
                return max(0, calls - len(timestamps))

        wrapper.rate_remaining = remaining
        return wrapper

    return decorator


@rate_limit(calls=3, per_seconds=5)
def api_call():
    print("API called")

# Try 5 calls quickly — the last two should raise RateLimitError
for i in range(5):
    try:
        api_call()
    except RateLimitError as e:
        print("Blocked:", e)
