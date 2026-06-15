import numpy as np
import sounddevice as sde
import random
def audiobit(freq,duration,freq_muestreo):
    #freq = 440;
    #duration =384.2;
    #freq_muestreo = 44100;
    zeit = np.linspace(0, duration, int(freq_muestreo * duration), endpoint=False)
    sinus = 0.5*np.sin(2*np.pi*freq*zeit)
    print("ha comenzado el juego")
    sde.play(sinus,freq_muestreo)
    f = int(input("si te duelen los oidos presiona un boton para salir\n"))
    if f<=1:
        sde.stop()
        return
    sde.wait()
    print("hemos terminado tio")
def main():
    print("amigo ha comenzado una batalla sin cuartel porfavor estate atento")
    while True:
        f = random.randint(1,15)

        audiobit(random.randint(50,200),f,44100)
        k = int(input("estoy a la espera de que me mandés algo jaja jeje jijji"))
        audiobit(k,f,44100)
if __name__ == "__main__":
    main()





