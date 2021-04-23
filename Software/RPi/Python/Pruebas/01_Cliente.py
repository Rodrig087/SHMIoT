import paho.mqtt.client as mqtt

broker_url = "181.39.228.231"
broker_port = 2283

#username = "cuxhjixd"
#password = "tFroIaJunMc6"

client = mqtt.Client()
#client.username_pw_set(username, password)
client.connect(broker_url,broker_port)

#client.publish(topic="TestingTopic", payload="Hola RSA_PC 2", qos=1, retain=False)
client.publish(topic="Chanlud/Acelerografo/1/Tiempo", payload="Hola RSA_PC 2", qos=1, retain=False)


client.loop_forever()