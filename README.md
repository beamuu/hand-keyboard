# Hand Keyboard (Keybong)

Keybong is a pair of gloves which acts like a keyboard on your computer. You can type texts without placing your hands on your keyboard.
Keybong detects your hand gesture and automatically type the text on your computer. Your computer and Keybong can be connected each other
when both of them are on the same network, and communication happens wirelessly.

### About project directories

- **`esp32/`** This directory contains the source code of the `NodeMCU ESP32` which communicate with the computer by using `socket` on the local network.
- **`comms/`** This contains the source code of the communication via `ESPNOW`, ESPNOW is the way how ESP32 communicate each other when they are in the same area.
- **`example-client.py`** This is a example client which will connect the `server.py` with socket (TCP/IP) when both client and server are running.
- **`server.py`** This is a `socket server` which will be run in your computer. This server allows Keybong to connect itself with your computer wirelessly (Only on the same network).
