import time

import serial
from constants import arduino_port

response_map = {'d': 7, 'u': 6}
connection = serial.Serial(arduino_port, timeout=1)


def send_command(cmd: str, response_len: int) -> str:
    connection.write(cmd.encode())
    str_resp = ""
    if response_len != 0:
        resp = connection.read(response_len)
        str_resp = resp.decode()
    return str_resp


while True:
    for command in response_map:
        resp = send_command(command, response_map[command])
        print(resp)
        time.sleep(1)
