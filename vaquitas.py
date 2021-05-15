import os
import random
import time
import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


inicioPuente = 10
largoPuente = 20
cantidadVacas = 5


semaforoVacas = threading.Semaphore(1)

class Vaca(threading.Thread):
    def __init__(self):
        super().__init__()
        self.posicion = 0
        self.velocidad = random.uniform(0.1, 0.9)

    def avanzar(self):
        while(self.posicion != inicioPuente):
            time.sleep(1-self.velocidad)
            self.posicion += 1
        if self.posicion == inicioPuente:
            logging.info('FINAL DEL PUENTE!')
            logging.info('FINAL DEL PUENTE!')
            logging.info('FINAL DEL PUENTE!')
            self.avanzarSemaforo()
    
    def avanzarSemaforo(self):
        semaforoVacas.acquire()
        while(self.posicion != largoPuente):
            logging.info('ARRANCA PT2!')
            time.sleep(1-self.velocidad)
            self.posicion += 1
        if self.posicion == largoPuente:
            logging.info('ARRANCA OTRA!')
            semaforoVacas.release()


    def dibujar(self):
        print(' ' * self.posicion + '🐮' + str()) # si no funciona, cambiá por 'V'


    def run(self):
        while(True):
            self.avanzar()

vacas = []
for i in range(cantidadVacas):
    v = Vaca()
    vacas.append(v)
    v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
    print(' ' * inicioPuente + '=' * largoPuente)

while(True):
    cls()
    print('Apretá Ctrl + C varias veces para salir...')
    print()
    dibujarPuente()
    for v in vacas:
        v.dibujar()
    dibujarPuente()
    time.sleep(0.2)