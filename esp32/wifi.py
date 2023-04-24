import network
import time

wlan = network.WLAN(network.STA_IF)

def connect():
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('WiFi Demo', '1122334455')
#         wlan.connect('R202 WiFi', '!q2w3e4r5t')
        while not wlan.isconnected():
            time.sleep_ms(100)
    print('network config:', wlan.ifconfig())

def disconnect():
#     if wlan.isconnected():
#         wlan.disconnect()
#     else:
#         wlan.disconnect()
#         wlan.active(False)
#         time.sleep_ms(1000)
#         wlan.active(True)
    wlan.disconnect()
    print("network disconnected")