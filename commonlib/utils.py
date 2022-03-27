import time
import uuid
from datetime import datetime, timedelta


def time_to_ms(time: float) -> int:
    return int(round(time * 1000))


def get_current_time_ms() -> int:
    return int(round(time.time() * 1000))


def time_str_to_int(timestr: str, fmt: str = "%Y-%m-%dT%H:%M:%S.%f") -> int:
    dt = datetime.strptime(timestr, fmt)
    timestamp = int((dt - datetime(1970, 1, 1)) / timedelta(microseconds=1))

    return timestamp


def time_int_to_str(timestamp: int, fmt: str = "%Y%m%d") -> str:
    dt = datetime.fromtimestamp(timestamp / 1000)
    return dt.strftime(fmt)


def is_valid_uuid(value: str) -> bool:
    try:
        uuid.UUID(value)

        return True
    except ValueError:
        return False
