# Bootcamp-PY-Herencia_Clases
Desafio Bootcamp - Python - Herencia de clases

El objetivo fue modelar distintos tipos de membresías para una aplicación de streaming de películas y series chilenas, aplicando conceptos como herencia, abstracción, encapsulamiento y reutilización de código mediante mixins.

## Archivos incluidos ##

- membresia.py: contiene la jerarquía de clases que representan los distintos tipos de membresía.
- test_membresia.py: script de prueba que permite al usuario crear y cambiar una membresía usando inputs desde la consola.

## Tipos de membresía ##

El sistema incluye los siguientes tipos:

1. Gratis
2. Básica
3. Familiar
4. Sin Conexión
5. Pro

Cada una tiene reglas distintas respecto a:

- Costo
- Cantidad máxima de dispositivos
- Días de regalo
- Permisos para cambiar de plan
- Acceso a funciones como control parental o visualización sin conexión

## Características del diseño ##

- Se utiliza una clase abstracta 'Membresia' como base para definir atributos comunes y el método obligatorio 'cambiar_suscripcion()'.
- Se utilizan mixins como clases auxiliares para agregar funcionalidades específicas, como días de regalo o cancelar suscripción.
- Se implementa herencia múltiple de forma controlada.
- Cada tipo de membresía valida a qué otros tipos puede cambiarse.
- El atributo 'dias_regalo' solo existe en las membresías que lo requieren.

## Cómo ejecutar el programa

1. Ejecuta el archivo de prueba desde la terminal:
        python test_membresia.py

2. El programa pedirá:

- Correo del suscriptor
- Número de tarjeta
- Opción de membresía a la que deseas cambiar

3. Verás en pantalla un resumen de la membresía actual, incluyendo:

- Tipo
- Costo
- Dispositivos permitidos
- Días de regalo (si aplica)
- Funciones disponibles como control parental o visualización offline