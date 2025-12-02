import time
import json
import random
from paho.mqtt import client as mqtt_client

broker = "localhost"
port = 1883
topic = "sensors/humidity"
client_id = "pub_humidity"

def connect():
    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    return client

def main():
    c = connect()
    while True:
        value = round(40 + random.random() * 20, 2)
        data = {"sensor": "humidity", "value": value}
        c.publish(topic, json.dumps(data))
        print("published:", data)
        time.sleep(3)

main()
