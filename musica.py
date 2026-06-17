import numpy as np
import sounddevice as sde
import random
import readchar
from readchar import key

notasportecla = {
    'w': (261, 2, 44100),
    'e': (294, 2, 44100),
    'r': (330,2,44100),
    't': (350,2,44100),
    'y': (392,2,44100),
    'u': (440,2,44100),
    'i': (494,2,44100),
}


def audiobit(freq,duration,freq_muestreo):
 
    zeit = np.linspace(0, duration, int(freq_muestreo * duration), endpoint=False)
    sinus = 0.5*np.sin(2*np.pi*freq*zeit)
    print("ha comenzado el juego")
    sde.stop()
    sde.play(sinus,freq_muestreo)
    print("hemos terminado tio")





def keydetectaudio(y):
    audiobit(*y)

    




def main():
    print("amigo ha comenzado una batalla sin cuartel porfavor estate atento")
    

    while True:
        teclis = readchar.readkey()
        if teclis  == 'q':
            sde.stop()
            print("adios")
            break
        elif teclis in notasportecla:
            keydetectaudio(notasportecla[teclis])

        
if __name__ == "__main__":
    main()












