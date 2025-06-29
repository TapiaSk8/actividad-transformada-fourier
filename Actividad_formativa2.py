import numpy as np
import matplotlib.pyplot as plt

#-----------Parámetros de muestreo-------------#
frecuencia_muestreo = 1000  # Hz
tiempo = np.linspace(-1, 1, 2 * frecuencia_muestreo, endpoint=False)  #2_duración

#-----------Definición de señales---------------#
pulso_rectangular = np.where(np.abs(tiempo) < 0.2, 1, 0)
escalon_unitario = np.where(tiempo >= 0, 1, 0)
senal_senoidal = np.sin(2 * np.pi * 50 * tiempo)  #50Hz

#-----------Función para graficar la FFT----------#
def graficar_fft(senal, titulo):
    N = len(senal)
    transformada = np.fft.fft(senal)
    frecuencias = np.fft.fftfreq(N, 1 / frecuencia_muestreo)

    plt.figure(figsize=(12, 4))

#-----------Magnitud------------#
    plt.subplot(1, 2, 1)
    plt.plot(frecuencias[:N // 2], np.abs(transformada[:N // 2]))
    plt.title(f'Magnitud del espectro - {titulo}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid(True)

#-------------Fase-------------#
    plt.subplot(1, 2, 2)
    plt.plot(frecuencias[:N // 2], np.angle(transformada[:N // 2]))
    plt.title(f'Fase del espectro - {titulo}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Fase (radianes)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

#---------------Diccionario de señales-------------#
senales = {
    'Pulso Rectangular': pulso_rectangular,
    'Escalón Unitario': escalon_unitario,
    'Señal Senoidal (50 Hz)': senal_senoidal
}

#---------Visualización en el dominio del tiempo y frecuencia----------#
for nombre, senal in senales.items():
    plt.figure(figsize=(8, 3))
    plt.plot(tiempo, senal)
    plt.title(f'Señal en el dominio del tiempo - {nombre}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    graficar_fft(senal, nombre)