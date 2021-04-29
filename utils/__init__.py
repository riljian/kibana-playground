from datetime import datetime


def gen_log(log_name, additional_payload=None):
    return {
        'name': log_name,
        'timestamp': datetime.timestamp(datetime.now()),
        **({} if additional_payload is None else additional_payload),
    }
