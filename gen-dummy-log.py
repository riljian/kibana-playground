import json
from datetime import datetime


class LogName:
    VEHICLE_REPORT = 'vehicle_report'


class Role:
    ADMINISTRATOR = 'administrator'
    CUSTOM_SERVICE = 'customer_service'


class Station:
    ADATA = 'Adata'


employees = [
    {
        'name': 'Jamie Lin',
        'role': Role.CUSTOM_SERVICE,
        'work_at': Station.ADATA,
    },
    {
        'name': 'Kuan Kuan',
        'role': Role.ADMINISTRATOR,
        'work_at': Station.ADATA,
    },
]

vehicles = [
    {
        'plate_number': 'ABC-123',
    },
]


def gen_vehicle_report_log():
    return {
        'latitude': 25,
        'longitude': 121,
        'g_sensor_x': 3,
        'g_senson_y': 4,
        'g_sensor_z': 5,
    }


def gen_log(log_name, additional_log_generator=lambda: {}):
    return {
        'name': log_name,
        'timestamp': datetime.timestamp(datetime.now()),
        **additional_log_generator(),
    }


with open('dummy-log.json', 'w') as f:
    log = gen_log(LogName.VEHICLE_REPORT, gen_vehicle_report_log)
    f.write(f"{json.dumps(log)}\n")
