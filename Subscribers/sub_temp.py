import time
from paho.mqtt import client as mqtt_client

broker = "localhost"
port = 1883
topic = "sensors/temperature"
client_id = "sub_temp"

logfile = "log_sub_temp.txt"

def on_message(client, userdata, msg):
    text = f"{time.time()}  {msg.topic}  {msg.payload.decode()}"
    print("received:", text)
    with open(logfile, "a") as f:
        f.write(text + "\n")

client = mqtt_client.Client(client_id)
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
