import paho.mqtt.client as mqtt

# broker = "test.mosquitto.org"
broker = "broker.hivemq.com"
port = 1883
topic = "psu/coe/influxdb"
client_id = "coe-mqtt-010"

# a callback function
def on_message_influxdb(client, userdata, msg):
    print("Received a new data ", str(msg.payload.decode("utf-8")))
    print("message topic=", msg.topic)
    print("message qos=", msg.qos)


# Give a name to this MQTT client
client = mqtt.Client(client_id)
client.message_callback_add(topic, on_message_influxdb)

# IP address of your MQTT broker, using ipconfig to look up it
client.connect(broker, port)
# 'psu/#' means subscribe all topic under psu
client.subscribe("psu/#")

client.loop_forever()
