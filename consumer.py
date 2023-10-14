import time

import paho.mqtt.client as mqtt

from constants import mqtt_broker_host, mqtt_topic, mqtt_broker_port


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


client = mqtt.Client()
client.on_connect = on_connect

client.connect(mqtt_broker_host, mqtt_broker_port, 60)

while True:
    message = input("Введите сообщение для отправки: ")
    client.publish(mqtt_topic, message)
    print(f"Отправлено сообщение: {message}")
    time.sleep(1)
