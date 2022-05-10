import paho.mqtt.client as mqtt #https://pypi.org/project/paho-mqtt/

# allback when receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT.- Connected with result code "+str(rc))
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)
    # if we lose the connection then subscriptions will be renewed.
    client.subscribe("/#")

# Callback when a PUBLISH message is received
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



client = mqtt.Client("Test")
client.on_connect = on_connect
client.on_message = on_message

#Replace XXXX with values corresponding to your Mosquitto configuration
client.username_pw_set(username="XXXX",password="XXXX")
client.connect("mosquitto", 1883, 60)

# Loop that keeps the script listening
client.loop_forever()