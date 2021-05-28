from os import name
import threading
import time
import logging
from random import randint

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaforoCocinero = threading.Semaphore(0)
semaforoPlato = threading.Semaphore(1)
semaforoComensales = threading.Semaphore(2)


class Cocinero(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Cocinero: {numero}'
        self.numero = numero

    def run(self):
        global platosDisponibles
        while (True):
            semaforoCocinero.acquire()
            try:
                logging.info('Reponiendo los platos...')
                platosDisponibles = 3
            finally:
                semaforoPlato.release()
                semaforoComensales.release()
                time.sleep(randint(0,2))

class Comensal(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Comensal {numero}'
        self.numero = numero

    def run(self):
        global platosDisponibles
        semaforoComensales.acquire()
        semaforoPlato.acquire()
        try:
            while platosDisponibles == 0:
                semaforoCocinero.release()
                semaforoPlato.acquire()
                semaforoComensales.acquire()
            platosDisponibles -= 1
            logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
        finally:
            semaforoPlato.release()
            semaforoComensales.release()

platosDisponibles = 3

for i in range(2):
    Cocinero(numero=i+1).start()

for i in range(50):
    Comensal(i).start()