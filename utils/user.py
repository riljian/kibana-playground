import secrets

import names

from models import Role


def gen_employees(amount):
    def get_employee(id):
        return {
            'id': id,
            'name': names.get_full_name(),
            'role': secrets.choice([Role.ADMINISTRATOR, Role.ENGINEER]),
        }
    return list(map(get_employee, range(amount)))
