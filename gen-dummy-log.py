import json
import secrets

from models import LogName
from utils import gen_log
from utils.vehicle import gen_vehicles
from utils.user import gen_employees
from utils.repair import gen_repair_log


def write_log(file_descriptor, log):
    file_descriptor.write(f"{json.dumps(log)}\n")


if __name__ == '__main__':
    employees = gen_employees(5)
    vehicles = gen_vehicles(5)

    with open('dummy-log.json', 'w') as f:
        for v in vehicles:
            log = gen_repair_log(creator=secrets.choice(employees),
                                 vehicle=secrets.choice(vehicles))
            write_log(f, log)
