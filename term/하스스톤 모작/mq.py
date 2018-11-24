import paho.mqtt.client as mqtt
from netplay import *
import _thread

topic = "hello/world"
myid="%02d" % randint(1,99)
client=mqtt.Client()
cardget=None

def on_connect(client, userdata, rc):
    print("Connected with result coe " + str(rc))

def on_message(client, userdata, msg):
    global cardget
    temp=msg.payload.decode('utf-8')
    if(temp[0:2] != myid):
        cardget=msg.payload.decode('utf-8')
        print("on-message")
        print(cardget)
    else:
        print("on-message")
        print("Sent by me")
def on_disconnect(client):
    print("Disconnected")

def sendok():
    global client
    pub=mqtt.Client()
    client.publish(topic,myid)
    print("published id")

def connect():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect=on_disconnect
    client.connect("broker.hivemq.com")
    print("connect")
    client.loop_start()
    client.subscribe(topic)
    print("called subscribe")
def disconnect():
    print("exiting")
    client.disconnect()
    client.loop_stop()
def tok():
    _thread.start_new_thread(sendok, ())


