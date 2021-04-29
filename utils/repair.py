from models import LogName
from utils import gen_log


def gen_repair_log(creator=None, vehicle=None):
    return gen_log(
        LogName.REPAIR_REPORT,
        {
            'creator': creator,
            'vehicle': vehicle,
        }
    )
