import time
import json
import random
from paho.mqtt import client as mqtt_client

broker = "localhost"
port = 1883
topic = "sensors/people"
client_id = "pub_people (12217586)"

def connect():
    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    return client

def main():
    c = connect()
    while True:
        value = random.randint(0, 10)
        data = {"sensor": "people", "value": value}
        c.publish(topic, json.dumps(data))
        print("published:", data)
        time.sleep(4)

main()
