
from ggenerate_wallet import GenerateWallets

modules_map = {
    "0": [exit],
    "1": [GenerateWallets.generate],

}


def get_module(number):
    return modules_map.get(number)
