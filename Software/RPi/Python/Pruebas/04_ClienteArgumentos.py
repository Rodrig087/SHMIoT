import paho.mqtt.client as mqtt
import sys

broker_url = "181.39.228.231"
broker_port = 2283

client = mqtt.Client()
client.connect(broker_url,broker_port)

client.publish(topic="Chanlud/Acelerografo/1/Tiempo", payload=sys.argv[1], qos=1, retain=False)
client.publish(topic="Chanlud/Acelerografo/1/Duracion", payload=sys.argv[2], qos=1, retain=False)

