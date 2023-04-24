from machine import Pin, ADC
import dht
import time
import urequests
import gc
import wifi
import json
import mqtt

# wifi.disconnect()
# print("Sleep for 10 seconds...")
# time.sleep(10)
wifi.connect()
mqtt.connect()
dht22 = dht.DHT22(Pin(14))
ldr = ADC(Pin(34))
raindrop = ADC(Pin(32))
data = dict()

# headers = {
#     'Authorization': 'Token UMKY6z06AaMyL7tQlX8_mqfNuY4r_S99wqzwX7sPtbD4-PXmcjxTdwcHJDLUWj8RnEtYrXUzR7K1QePDorDzOg==',
#     'Content-Type': 'text/plain; charset=utf-8',
#     'Accept': 'application/json',
#     }

def get_ldr_value():
    raw_data = ldr.read_u16()
    data = round(raw_data/65535*100, 2)
    if data > 0:
        return data
    else:
        return 0

def get_raindrop_value():
    adc_raindrop = raindrop.read_u16()
#     print(adc_raindrop)
    data = round(100.0 - (adc_raindrop/65535*100.0), 2)
    if data > 0:
        return data
    else:
        return 0

# def post_data(temerature, humidity, light):
#     gc.collect()
#     data = f'measurement,sensor_id=s002 temperature={temperature},humidity={humidity},light={light}'
#     print("Data:", data)
#     try:
#         response = urequests.request(method="POST",
#                               url="http://192.168.1.12:8086/api/v2/write?org=psu&bucket=all_about&precision=ns",
#                               headers=headers,
#                               data=data)
#         print(response.__dict__)
#     except OSError as e:
#         print("Cannot send data:", e)
#     gc.collect()


while True:
    print("----------------------------------------------")
    try:
        dht22.measure()
        time.sleep_ms(100)
        temperature = dht22.temperature()
        humidity = dht22.humidity()
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity} %")
    except OSError as e:
        print("Cannot read DHT22:", e)
        
    light_value = get_ldr_value()
    if light_value > 0:
        print(f"Light: {light_value} %")
    else:
        print("Cannot read light sensor:", light_value)
    raindrop_value = get_raindrop_value()
    print(f"Raindrop: {raindrop_value} %")
    data["temperature"] = temperature
    data["humidity"] = humidity
    data["light"] = light_value
    data["raindrop"] = raindrop_value
    mqtt.publish(data)
    time.sleep_ms(1000)
