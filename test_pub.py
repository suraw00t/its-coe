import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from datetime import datetime
import json

mqttBroker = "mqtt.eclipseprojects.io"
client_id = "coe-mqtt-001"
topic = "psu/coe/influxdb"

client = mqtt.Client(client_id)
client.connect(mqttBroker)

while True:
    randNumber = uniform(24.0, 26.0)
    data = {"temperature": randNumber, "timestamp": datetime.now().timestamp()}
    data_json = json.dumps(data)
    client.publish(topic=topic, payload=str(data_json))
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
