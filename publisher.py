import time

import paho.mqtt.client as mqtt

from constants import mqtt_broker_host, mqtt_topic, mqtt_broker_port, mqtt_status_topic


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_status_topic)


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Message received: {message}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker_host, mqtt_broker_port, 60)

while True:
    client.loop_start()
    message = input("Введите сообщение для отправки: ")
    client.publish(mqtt_topic, message)
    print(f"Отправлено сообщение: {message}")
    time.sleep(1)
