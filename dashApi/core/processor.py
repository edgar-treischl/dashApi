# processor.py
import time

start_time = time.time()


def get_uptime() -> float:
    return round(time.time() - start_time, 2)


def get_ping_response() -> dict:
    return {"message": "pong", "uptime_seconds": get_uptime()}
