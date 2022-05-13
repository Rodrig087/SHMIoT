#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import json

#Credenciales del Broker MQTT:
broker_url = "181.39.228.231"												    #URL del broker remoto
broker_port = 2283																#Puerto por donde se comunica el broker

#Topicos:
topicoPeticion	= "Chanlud/Acelerografo/Prueba/Peticion"
topicoRespuesta	= "Chanlud/Acelerografo/Prueba/Respuesta"								

#Variables:
contador = 0

evento_out = {"Fecha":"210430", "Hora":"151515", "Duracion":"36"}
data_out = json.dumps(evento_out)

#Metodos:
def on_connect(client, userdata, flags, rc):
   print("Conexion con codigo de resultado " + str(rc))
   
def on_disconnect(client, userdata, rc):
   print("Cliente desconectado")

def on_message(client, userdata, message):
   
   print("Solicitud recibida")
   #Decodificacion peticion recibida:
   peticion = message.payload.decode()
   
   #Decodificacion mensaje JSON:
   m_in=json.loads(peticion) 
   print(type(m_in))
   print("Fecha = ",str(m_in["F"]))
   print("Hora = ",str(m_in["H"]))
   print("Segundos = ",str(m_in["Hs"]))
   print("Duracion = ",str(m_in["D"]))
   
   if peticion == chr(64):
      print("Solicitud de peticion")
      responder(topicoRespuesta,data_out)
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




