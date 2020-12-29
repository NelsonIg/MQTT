#! /usr/bin/env python3

from con_nodemcu import send_udp
import sys
import paho.mqtt.client as mqtt

remote_msg = send_udp(('192.168.137.176',8888), 'Hallo from client_pub')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global remote_msg
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.publish("nodemcu/", payload=remote_msg)
    client.disconnect()
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
#client.on_message = on_message

client.connect('localhost', 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

