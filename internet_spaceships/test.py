import json
import random
import subprocess
import firmware


def test(ship):
    read_data = open('test_files/input.json').read()
    # print json.loads(read_data)
    # input_data = json.dumps(json.loads(read_data))
    subprocess.call("python firmware.py '{}'".format(read_data), shell=True)


if __name__ == '__main__':
    ship = firmware.Firmware()
    test(ship)
