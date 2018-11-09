import time
from websocket import create_connection

ws = create_connection("ws://flyinguziteamproject:9999/")

while True:
    ws.send("Hello, World")
    time.sleep(1)
    result = ws.recv()
    print("Received '%s'" % result)
    time.sleep(1)

ws.close()
