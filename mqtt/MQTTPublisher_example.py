import paho.mqtt.client as mqtt #https://pypi.org/project/paho-mqtt/

client = mqtt.Client("Test Pub")

#Replace XXXX with values corresponding to your Mosquitto configuration
client.username_pw_set(username="XXXX",password="XXXX")
client.connect("mosquitto", 1883, 60)
client.publish("#/Temp",123)

client.publish("#/Temp","{temp:24}") #Submit your desired JSON