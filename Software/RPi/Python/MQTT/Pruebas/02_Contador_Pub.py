#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time


#Configuracion del cliente MQTT:
broker_url = "181.39.228.231"
broker_port = 2283

#username = "cuxhjixd"															#Nombre de usuario definido en el broker remoto
#password = "tFroIaJunMc6"														#Contrasena definida en el broker

client = mqtt.Client()															#Crea un instancia de Client
#client.username_pw_set(username, password)										
client.connect(broker_url,broker_port)


#Variables:
contador = 0


while (True):
    contador = contador+1
    #client.publish(topic="Contador", payload=contador, qos=1, retain=False)
    client.publish(topic="Chanlud/Acelerografo/1/Tiempo", payload=contador, qos=1, retain=False)
    #print(contador)
    time.sleep(1)
    client.loop_start()
    client.loop_stop()

