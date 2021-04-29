from models import Role, Station

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
        'vcu_ble_mac': 'FF:FF:FF:FF:FF:FF',
    },
    {
        'plate_number': 'DEF-456',
        'vcu_ble_mac': '00:00:00:00:00:00',
    },
]
