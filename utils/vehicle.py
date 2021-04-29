from uuid import uuid4


exists_plate_number = set()
exists_mac_address = set()


def gen_plate_number():
    while True:
        template = f'{uuid4()}'.replace('-', '')[:6]
        plate_number = f'{template[:3]}-{template[3:]}'.upper()
        if plate_number not in exists_plate_number:
            exists_plate_number.add(plate_number)
            return plate_number


def gen_mac_address():
    while True:
        template = f'{uuid4()}'.replace('-', '')[:12]
        split_len = 2
        template_chunks = [template[i:i + split_len]
                           for i in range(0, len(template), split_len)]
        mac_address = ':'.join(template_chunks).upper()
        if mac_address not in exists_mac_address:
            exists_mac_address.add(mac_address)
            return mac_address


def gen_vehicles(amount):
    def get_vehicle(id):
        return {
            'id': id,
            'plate-number': gen_plate_number(),
            'vcu_ble_mac': gen_mac_address(),
        }
    return list(map(get_vehicle, range(amount)))
