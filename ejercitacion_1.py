import random
import time
import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


semaforoPatio = threading.Semaphore(1)


class Patio():
    def __init__(self):
        self.estaOcupado = False
        self.nombre = "Patio"
    
    def __str__(self):
        return self.nombre

patiooo = Patio()

class Animal(threading.Thread):
    def __init__(self):
        super().__init__()
        self.nombre = "animalBase"
    
    def entrarAlPatio(self):
        semaforoPatio.acquire()
        while(True):
            try:
                if(patiooo.estaOcupado == False):
                    patiooo.estaOcupado = True
                    logging.info(f'el {self.nombre} esta en el patio.')
                    time.sleep(random.randint(1,3))
                    patiooo.estaOcupado = False
                    logging.info('el patio esta libre!')
            finally:
                semaforoPatio.release()
                


    def run(self):
        while(True):
            self.entrarAlPatio()


class Perro(Animal):
    def __init__(self):
        super().__init__()
        self.nombre = "Perro"

class Gato(Animal):
    def __init__(self):
        super().__init__()
        self.nombre = "Gato"



animales = []
gatito = Gato()
perrito = Perro()
animales.append(perrito)
animales.append(gatito)
for animal in animales:
    animal.start()

while(True):
    time.sleep(0.2)
    if not(patiooo.estaOcupado):
        logging.info(f'No hay animales en el {patiooo}')





