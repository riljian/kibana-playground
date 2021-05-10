from datetime import datetime, timedelta
import random

from models import LogName
from utils import gen_random_datetime_between_range, trans_unix_ms_timestamp


def gen_repair_log(creator=None, vehicle=None, repair_items=None):
    now = datetime.now()
    delta = timedelta(days=7)
    random_datetime = gen_random_datetime_between_range(now - delta, now)
    return {
        'name': LogName.REPAIR_REPORT,
        'timestamp': trans_unix_ms_timestamp(random_datetime),
        'creator': creator,
        'vehicle': vehicle,
        'consume_items': list(map(lambda item: {**item, 'amount': random.randrange(1, 10, 1)}, repair_items)),
    }
