import time
import json
import random
from paho.mqtt import client as mqtt_client

broker = "localhost"
port = 1883
topic = "sensors/temperature"
client_id = "pub_temp (12217586)"

def connect():
    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    return client

def main():
    c = connect()
    while True:
        value = round(20 + random.random() * 5, 2)
        data = {"sensor": "temperature", "value": value}
        c.publish(topic, json.dumps(data))
        print("published:", data)
        time.sleep(2)

main()
