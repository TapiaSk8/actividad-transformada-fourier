Actividad formativa 2. Simulación y análisis de señales con la transformada de Fourier

Este proyecto forma parte de una actividad donde analicé señales en el dominio del tiempo y la frecuencia usando Python. Apliqué la Transformada de Fourier para ver cómo se comportan diferentes señales y qué información se puede obtener de su espectro.

objetivo:

Entender cómo se representan las señales en el dominio de la frecuencia y comprobar propiedades importantes de la Transformada de Fourier como:

- Linealidad
- Desplazamiento en el tiempo
- Escalamiento en frecuencia

Herramientas utilizadas:

- Python 3
- NumPy
- Matplotlib

Señales analizadas:

- Pulso rectangular
- Escalón unitario
- Señal senoidal (50 Hz)

Cada señal fue graficada en el dominio del tiempo y luego se le aplicó la Transformada de Fourier para obtener su espectro (magnitud y fase).

Propiedades verificadas:

- **Linealidad:** La suma de señales produce un espectro que es la suma de los espectros individuales.
- **Desplazamiento en el tiempo:** No cambia la magnitud del espectro, pero sí la fase.
- **Escalamiento en frecuencia:** Al aumentar la frecuencia de una señal, su espectro también se desplaza.

Cómo ejecutar el código:

1. Asegúrate de tener Python instalado.
2. Instala las librerías necesarias:

   CMD
   pip install numpy matplotlib
