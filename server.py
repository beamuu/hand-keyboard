import socket
import sys
import _thread
from pynput.keyboard import Key, Controller

keyboard = Controller()

server_address = ("", 3000)

print(sys.stderr, "starting up on %s port %s" % server_address)

connections = []

caps = False

def decodeBytes(b):
    return b.decode("utf-8")

def broadcast(what):
    for c in connections:
        c.sendall(what)

def keyboardType(what):
    return keyboard.type(str(what))


def on_new_client(clientsocket,addr):
    global caps
    while True:
        try:
            msg = clientsocket.recv(1024)
            cmds = msg.decode("utf-8").split(';')
            for cmd in cmds:
                print(cmd)
                if (":" not in cmd):
                    continue
                who = cmd.split(":")[0]
                key = cmd.split(":")[1]
                if who == 'B':
                    if caps:
                        keyboardType(key.upper())
                    else:
                        keyboardType(key.lower())
                elif who == 'N':
                    if key == 'E':
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                    elif key == 'C':
                        keyboard.press(Key.caps_lock)
                        keyboard.release(Key.caps_lock)
                        caps = not caps
                    elif key == 'B':
                        keyboard.press(Key.backspace)
                        keyboard.release(Key.backspace)
            
        except:
            exit(1)
    # clientsocket.close()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(server_address)
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"Connected from {addr}")
        _thread.start_new_thread(on_new_client,(conn,addr))
        connections.append(conn)
