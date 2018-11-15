import time
import sys
from gpiozero import OutputDevice as stepper
IN1 = stepper(12)
IN2 = stepper(16)
IN3 = stepper(20)
IN4 = stepper(21)
stepPins = [IN1,IN2,IN3,IN4] # Pines del motor
stepDir = -1 # 1 = Sentido de las agujas del reloj
             # -1 = Sentido contrario a las agujas del reloj
mode = 1 # mode = 1: Baja Velocidad ==> Mas Potencia
         # mode = 0: Mas velocidad ==> Menos potencia
if mode: # Baja velocidad ==> Mas potencia
    seq = [[1,0,0,1], # Definir la secuencia como indica el fabricante
        [1,0,0,0], 
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]]
else: # Mas velocidad ==> Menos potencia 
    seq = [[1,0,0,0], # Definir la secuencia como indica el fabricante
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]]
stepCount = len(seq)
if len(sys.argv)>1: # Leer el tiempo de espera de la línea de comandos
    waitTime = int(sys.argv[1])/float(1000)
else:
    waitTime = 0.004 # Si no, por defecto seran 4 ms

stepCounter = 0

while True: # Bucle principal
    for pin in range(0,4):
        xPin=stepPins[pin] # Obtener GPIO
        if seq[stepCounter][pin]!=0:
            xPin.on()
        else:
            xPin.off()
    stepCounter += stepDir
    if (stepCounter >= stepCount):
        stepCounter = 0
    if (stepCounter < 0):
        stepCounter = stepCount+stepDir
    time.sleep(waitTime) # Esperar antes de mover
