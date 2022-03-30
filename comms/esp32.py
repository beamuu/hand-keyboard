import network
from esp import espnow

w0 = network.WLAN(network.STA_IF)
w0.active(True)

import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(scl=Pin(22),sda=Pin(21),freq=100000)


e = espnow
e.init()
pBon = b'\xe8\x68\xe7\x19\xaa\xb0'   
e.add_peer(pBon)
pNik = b'\xe8\xbd\x84\x00\xd9\xe8'   
e.add_peer(pNik)


def rx(result):
    mac, msg = result
    byt = chr(ord(msg))
    tmp = ""
    if mac == pBon :
        tmp += "B:"
    else :
        tmp += "N:"
    tmp += msg.decode("utf-8")
    print(bytes(tmp, "utf-8"))
    a = bytes(tmp, "utf-8")
    i2c.writeto(0x50, a)
    print("Receive data from STM32:OK")
    print("recv: %s - %s" % (mac,msg))
    
while True:
    time.sleep(0.2)
    msg = e.on_recv(rx)