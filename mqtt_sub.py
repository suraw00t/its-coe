import paho.mqtt.client as mqtt
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from datetime import datetime

bucket = "itscoe-bucket"

client = InfluxDBClient(url="http://localhost:8086", token="its-all-about-the-computer-engineering", org="coe-psu")
write_api = client.write_api(write_options=SYNCHRONOUS)

client_id = "coe-mqtt-005"


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(datetime.now(), "received message:", payload)
    #data_json = json.loads(payload)
    #p = Point("measurement").tag("device_id", "s001").field("temperature", float(data_json["temperature"]))
    #write_api.write(bucket=bucket, record=p)
    #p = Point("measurement").tag("device_id", "s001").field("humidity", float(data_json["humidity"]))
    #write_api.write(bucket=bucket, record=p)
    #p = Point("measurement").tag("device_id", "s001").field("light", float(data_json["light"]))
    #write_api.write(bucket=bucket, record=p)
    #p = Point("measurement").tag("device_id", "s001").field("raindrop", float(data_json["raindrop"]))
    #write_api.write(bucket=bucket, record=p)


#mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "localhost"
topic = "mymqtt/sensors"

client = mqtt.Client(client_id)
client.connect(mqttBroker)

client.loop_start()

client.subscribe(topic)
client.on_message = on_message

#time.sleep(86400)
while True:
    time.sleep(1)
client.loop_stop()
