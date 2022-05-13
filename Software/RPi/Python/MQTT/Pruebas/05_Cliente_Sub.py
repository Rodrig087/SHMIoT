#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time


#Credenciales del Broker MQTT:
broker_url = "181.39.228.231"												    #URL del broker remoto
broker_port = 2283																#Puerto por donde se comunica el broker
#username = "gateway1"															#Nombre de usuario definido en el broker remoto
#password = "smapfcgw1"															#Contrasena de usuario

#Topicos:
#topicoPeticion = "chanlud/lectura/gateway/1"									#Topico de peticion
#topicoRespuesta = "chanlud/respuesta/gateway/1"								#Topico de respuesta
#topicoPeticion_Tiempo = "Chanlud/Acelerografo/Prueba/Tiempo"									
#topicoPeticion_Duracion = "Chanlud/Acelerografo/Prueba/Duracion"
topicoPeticion	= "Chanlud/Acelerografo/Prueba/Peticion"
topicoRespuesta	= "Chanlud/Acelerografo/Prueba/Respuesta"								

#Variables:
contador = 0

#Metodos:
def on_connect(client, userdata, flags, rc):
   print("Coneccion con codigo de resultado " + str(rc))
   
def on_disconnect(client, userdata, rc):
   print("Cliente desconectado")

def on_message(client, userdata, message):
   print("Solicitud recibida")
   peticion = message.payload.decode()
   if peticion == chr(64):
      print("Solicitud de peticion")
      responder(topicoRespuesta,"Hola Mundo!!!")
   else:
      print("Mensaje recibido: "+str(peticion))
      responder(topicoRespuesta,peticion)

def responder(topico, dato):
   client.publish(topic=topico, payload=dato, qos=1, retain=False)   
   
 
#Crea un instancia de Client:
client = mqtt.Client()															
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

#Establece la conexion al Broker:
#client.username_pw_set(username, password)										
client.connect(broker_url,broker_port)

client.subscribe(topicoPeticion, qos=1)											#Se suscribe al topico de peticion

client.loop_forever()




