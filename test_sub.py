import paho.mqtt.client as mqtt
import time

topic = "psu/coe/influxdb"
client_id = "coe-mqtt-002"


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


mqttBroker = "mqtt.eclipseprojects.io"
topic = "psu/coe/influxdb"

client = mqtt.Client(client_id)
client.connect(mqttBroker)

client.loop_start()

client.subscribe(topic)
client.on_message = on_message

time.sleep(180)
client.loop_stop()
