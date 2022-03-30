import time, network, socket
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import os

i2c = I2C(scl=Pin(22),sda=Pin(21),freq=100000)

led = Pin(2, Pin.OUT)
led.value(0)

# Initialize network
station = network.WLAN(network.STA_IF)
station.active(True)

# Network to connect
NETWORK_NAME = "N!K's Laptop"
NETWORK_PASSWORD = "6210eiei"

connected = False

while not connected:
    print('Try connecting to WiFi ->', NETWORK_NAME, '...')
    station.connect(NETWORK_NAME, NETWORK_PASSWORD)
    connected = station.isconnected()
    time.sleep(4)
host = "192.168.137.96"
port = 3000

print(station.ifconfig())
IP, SUBNET_MASK, GATEWAY, DNS = station.ifconfig()

# CAPS state


def creatingSocketConnection():
    print("Beginning socket connection...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return s, True
    except:
        return None, False


device_connected = False
s = None
while not device_connected:
    time.sleep(1)
    led.value(0)
    s, device_connected = creatingSocketConnection()
    time.sleep(1)
    led.value(1)

led.value(1)


def rx(result):
    mac, msg = result
    byt = str(ord(msg))
    print("recv: %s - %s" % (mac, msg))


while True:
    time.sleep(0.5)
    try:
        msgFromBoard = i2c.readfrom(0x50, 3)
        text = msgFromBoard.decode()
    except:
        continue
    
    print(msgFromBoard)
    if text == "EMP":
        continue
    msgToSend = text+";"
    try:
        s.sendall(bytes(msgToSend, "utf-8"))
    except OSError:
        continue
    

