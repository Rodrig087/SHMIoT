from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

pathFile = "/home/pi/TMP/EventosDetectados.tmp"

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(event.src_path, "modificado.")
    
    def on_created(self, event):
        print(event.src_path, "creado.")
    
    def on_moved(self, event):
        print(event.src_path, "movido a", event.dest_path)
    
    def on_deleted(self, event):
        print(event.src_path, "eliminado.")

observer = Observer()
observer.schedule(MyEventHandler(), pathFile, recursive=False)
observer.start()

try:
    while observer.is_alive():
        observer.join(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

#************************************************************************************************
###Importate###
#Revisar que la version de la libreria watchdog sea compatible con la version de Python instalada
#Las estaciones trabajan con Python 3.5.3
#La version compatible de la libreria watchdog  es la 0.10.6
#Intalacion: sudo pip3 install watchdog==0.10.6
#Instalacion pip3: sudo apt-get install python3-pip 
#            sudo pip3 install --upgrade setuptools
#************************************************************************************************