import random
from datetime import datetime


def gen_random_datetime_between_range(datetime_from, datetime_to):
    timestamp_from = datetime.timestamp(datetime_from)
    timestamp_to = datetime.timestamp(datetime_to)
    random_timestamp = \
        timestamp_from + random.random() * (timestamp_to - timestamp_from)
    return datetime.fromtimestamp(random_timestamp)


def trans_unix_ms_timestamp(original):
    return int(datetime.timestamp(original) * 1000)
