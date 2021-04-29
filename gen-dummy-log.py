import json

from models import LogName
from utils import gen_log
from utils.vehicle import gen_big_data_report_log
from fixtures import vehicles


def write_log(file_descriptor, log):
    file_descriptor.write(f"{json.dumps(log)}\n")


with open('dummy-log.json', 'w') as f:
    for v in vehicles:
        additional_payload = gen_big_data_report_log(v)
        write_log(f, gen_log(LogName.VEHICLE_REPORT, additional_payload))
