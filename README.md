# **Predicción de Distancia Comóvil en Cosmología**

**Alumna:** Yamile Montecinos Rodríguez  
**Asesor:** Dr. Sebastien Mickael Marc Fromenteau  

El objetivo de este proyecto es desarrollar un modelo de aprendizaje automático capaz de predecir la distancia comóvil en cosmología a partir de parámetros fundamentales del universo:

- $z$ (redshift)
- $H_0$ (constante de Hubble)
- $\Omega_m$ (densidad de materia)
- $\Omega_\lambda$ (densidad de energía oscura)

Se busca comparar la predicción de la red neuronal con la distancia comóvil calculada mediante integración numérica, ofreciendo una alternativa rápida y precisa.

## Archivos Disponibles
- `tools.py`: Contiene funciones fundamentales para calcular la distancia comóvil de manera numérica.
- `crear_bd.ipynb`: Genera un dataset sintético de 50,000 muestras de parámetros cosmológicos y sus correspondientes distancias comóviles, guardándolo en un archivo CSV.
- `regresion.ipynb`: Entrena una red neuronal para predecir la distancia comóvil a partir de los parámetros cosmológicos. Incluye métricas de evaluación en el conjunto de entrenamiento y prueba. También se hace una prueba del modelo utilizando nuevos datos aleatorios.
- `predecir_distancia_comovil.ipynb`: Presenta una función que permite predecir la distancia comóvil dado los parámetros $z$, $H_0$, $\Omega_m$ y $\Omega_\lambda$, comparando la predicción de la red neuronal con el valor calculado numéricamente.
- `resources/`:
    * `bd_distancia_comovil.csv`: Base de datos del proyecto.
    * `modelo_distancia_comovil.h5`: Red neuronal entrenada.
    * `scaler.pkl`: Scaler para normalización de datos de entrada.
- `imágenes/`: Gráficas generadas.

## Resultados del Modelo
**Conjunto de entrenamiento:**
- MAE = 0.0094
- MSE = 0.0013
- R² = 0.9908

**Conjunto de prueba:**
- MAE = 0.0100
- MSE = 0.0016
- R² = 0.9891

El modelo predice la distancia comóvil con alta precisión, siendo una alternativa eficiente a los cálculos integrales numéricos.

## Uso del Programa
- Si se desea realizar el proceso de entrenamiento:
    * Primero se debe ejecutar `crear_bd.ipynb` para generar la base de datos empleada para el entrenamiento del modelo.
    * Después se ejecuta `regresion.ipynb` para entrenar la red neuronal y probar su desempeño con nuevos datos aleatorios.
- Si sólo se quiere utilizar el predictor:
    * Únicamente se debe ejecutar `predecir_distancia_comovil.ipynb`, ya que el notebook carga automáticamente el modelo ya entrenado junto con el scaler empleado para normalizar los datos.
    * Se requiere ingresar los valores de $z$, $H_0$, $\Omega_m$ y $\Omega_\lambda$ deseados para obtener la predicción y compararla con el cálculo numérico.

## Contacto
LinkedIn: [@yamilemontecinos](https://www.linkedin.com/in/yamilemontecinos/)  
Correo electrónico: yamile.montecinos@uaem.edu.mx  