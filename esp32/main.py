import time, network, socket
from machine import Pin, I2C
import network
from esp import espnow

led = Pin(2, Pin.OUT)
led.value(0)

# Initialize network
station = network.WLAN(network.STA_IF)
station.active(True)

# Network to connect
NETWORK_NAME = "Beamu"
NETWORK_PASSWORD = "123456789x"

connected = False

while not connected:
    print("Try connecting to WiFi...")
    station.connect(NETWORK_NAME, NETWORK_PASSWORD)
    connected = station.isconnected()
    time.sleep(4)

print(station.ifconfig())
IP, SUBNET_MASK, GATEWAY, DNS = station.ifconfig()

# Connection between ESP32

e = espnow
e.init()
pBon = b'\xe8\x68\xe7\x19\xaa\xb0'   # MAC address of peer's wifi interface b'\xe8\x68\xe7\x19\xaa\xb0'  bon
e.add_peer(pBon)
pNik = b'\xe8\xbd\x84\x00\xd9\xe8'   # MAC address of peer's wifi interface b'\xe8\xbd\x84\x00\xd9\xe8' nik
e.add_peer(pNik)

# CAPS state

host = "172.20.10.5"
port = 8000

    
def creatingSocketConnection():
    print("Beginning socket connection")
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
    print("recv: %s - %s" % (mac,msg))

while True:
    msg = e.on_recv(rx)     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        #i2c.writeto(0x50,msg)
        print(msg)
        s.sendall(msg)
        #print("me")
        #byt = str(msg)
        #i2c.writeto(0x50,byt)
        if msg[1] == b'end':
            break
