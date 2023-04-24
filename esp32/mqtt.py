from umqtt.simple import MQTTClient
import json

broker = "172.30.222.54"
client_id = "its-coe-00"
topic = "mymqtt/sensors"

client = MQTTClient(client_id, broker, keepalive=60)

def connect():
    print("connecting to MQTT Server...")
    client.connect()
    
def publish(data):
    data_json = json.dumps(data)
    print("msg:", data_json)
    client.publish(topic.encode(), data_json.encode())