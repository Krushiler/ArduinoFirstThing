import time

import paho.mqtt.client as mqtt
import serial

from constants import mqtt_broker_host, mqtt_topic, mqtt_broker_port, arduino_port, mqtt_status_topic

ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")
    ser.write(message.encode())


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker_host, mqtt_broker_port, 60)
client.loop_start()

while True:
    line = ser.readline()
    if line:
        client.publish(mqtt_status_topic, str(line))
    time.sleep(1)
