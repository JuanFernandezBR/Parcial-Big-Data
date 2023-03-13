# Parcial-Big-Data
Parcial primer corte de Big Data

Realizado por:
* Juan Pablo Fernández Barragan
* David Zarate

Parcial I – Big_data e Ing. De Datos
(máximo 2 estudiantes, los 2 puntos son obligatorios sin importar el número de estudiantes)

1- Usando zappa crear una función lambda que descargue la primera página de resultados del sitio Finca Raiz(https://www.fincaraiz.com.co) para la venta de casas en el sector de chapinero.
Esta lambda se debe ejecutar todos los lunes a las 9 am.
La página html se debe guardar en un bucket s3://landing-casas-xxx/yyyy-mm-dd.html


2 - Al llegar la página web al bucket se debe disparar un segundo lambda que procese el archivo utilizando el paquete de python beatifulsoup y extraiga la información de cada casa.
Se debe crear un archivo CSV en s3://casas-final-xxx/yyyy-mm-dd.csv con la siguiente estructura de columnas:
FechaDescarga, Barrio, Valor, NumHabitaciones, NumBanos, mts2
