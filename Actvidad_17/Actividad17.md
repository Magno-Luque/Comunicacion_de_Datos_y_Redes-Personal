# Actividad 17

## Problema 1: Simulación de un cliente-servidor

Conceptos: Cliente, Servidor, Protocolo, TCP/IP

Escribe una función en Python que simule la comunicación entre un cliente y un servidor usando la programación funcional. El cliente debería ser capaz de enviar mensajes y el servidor de responder de acuerdo con un protocolo simple (por ejemplo, eco, reverso del mensaje, etc.).

+ Implementa funciones separadas para el comportamiento del cliente y del servidor.
+ Simula el envío y recepción de mensajes.
+ Aplica conceptos de TCP/IP en un contexto abstracto.

**Respuesta 1:**

Paso 1: Definir las funciones del servidor.

```bash
def servidor(mensaje):
    """Procesa los mensajes enviados por el cliente según el comando especificado."""
    comando, _, contenido = mensaje.partition(':')
    if comando.strip().lower() == 'eco':
        return contenido.strip()
    elif comando.strip().lower() == 'reverso':
        return contenido.strip()[::-1]
    else:
        return "Comando no reconocido."
```
El servidor debe ser capaz de interpretar el mensaje recibido y responder de acuerdo al comando especificado en el mensaje.

Paso 2: Definir la función cliente.

```bash
def cliente(mensaje):
    """Enviar los mensajes al servidor y procesar la respuesta."""
    respuesta = servidor(mensaje)
    print(f'Servidor dice: {respuesta}')
```

Paso 3: Simulación de la comunicación. Llamaremos a la función cliente con diferentes mensajes.

```bash
def main():
    cliente("eco: Hola Mundo")
    cliente("reverso: Hola Mundo")
    cliente("sumar: 123 + 456")
    
if __name__ == "__main__":
    main()
```

### Ejercicio para extender la simulación
+ Agregar más comandos: Implementa más funcionalidades en el servidor, como sumar números o convertir el mensaje a mayúsculas.
+ Validación de mensajes: Agregar validaciones para asegurarte de que los mensajes sigan el formato correcto antes de procesarlos.
+ Simular retrasos de Red: Introduce retrasos aleatorios para simular la latencia de la red y observa cómo afecta la comunicación. 

Mi respuesta:

```bash
# Importamos librerías
import re  # módulo que proporciona operaciones de coincidencia
import random as rd
import time # módulo que permite trabajar con el tiempo

# Modificación de funciones 
def servidor(mensaje):
    """Procesa los mensajes enviados por el cliente según el comando especificado."""
    mensaje = mensaje.upper() # convertimos el mensaje a mayúsculas
    retraso = rd.uniform(0,5) # simulamos retrasos de Red
    print("------")
    print("Procesando solicitud...")
    time.sleep(retraso)
    if re.match("^[A-Z:0-9\s+]+$",mensaje): # validación de mensajes
        comando, _, contenido = mensaje.partition(':')
        
        if comando.strip() == 'ECO':
            return contenido.strip(), retraso
        elif comando.strip() == 'REVERSO':
            return contenido.strip()[::-1], retraso
        elif comando.strip() == 'SUMAR':  # sumar números
            numeros = [int(i) for i in contenido.split('+')]
            suma = sum(numeros)
            return suma, retraso
        else:
            return "Comando no reconocido.", retraso
    else:
        return "El mensaje contiene caracteres no permitidos.", retraso
    
def cliente(mensaje):
    """Enviar los mensajes al servidor y procesar la respuesta."""
    respuesta, retraso = servidor(mensaje)
    print(f'Servidor dice: {respuesta}')
    print(f'{retraso:.2f} segundos en responder...')
    
def main():
    cliente("eco: Hola Mundo")
    cliente("reverso: Hola Mundo")
    cliente("sumar: 123 + 456")
    cliente("sumar: @")
    
if __name__ == "__main__":
    main()
```

---
## Problema 4: Simulación del modelo OSI

Conceptos: Modelo OSI, Encapsulación de Datos, Protocolo Stack

Desarrolla una serie de funciones que simulan la transmisión de datos a través de las diferentes capas del modelo OSI, mostrando cómo se encapsulan y desencapsulan los datos en cada capa.

+ Implementa funciones que representen cada capa del modelo OSI.
+ Simula el proceso de encapsulación y desencapsulación de datos.

**Respuesta 4:**

Para abordar este problema, implementaremos un conjunto de funciones que simulan el proceso de transmisión de datos a través de las diferentes capas del modelo OSI (Open Systems Interconnection). Cada función representerá una capa del modelo y demostrará cómo los datos se encapsulan y desencapsulan a medida que pasan de una capa a otra.

El modelo OSI tiene siete capas:

+ Capa de aplicación
+ Capa de presentación
+ Capa de sesión
+ Capa de transporte
+ Capa de red
+ Capa de enlace de datos 
+ Capa física

Paso 1: Definir las funciones de cada capa.

Vamos a definir una función para cada capa, que recibirá los datos de la capa superior, añadirá su propia "cabecera" (simulando la encapsulación), y luego pasará los datos a la siguiente capa.

```bash
def capa_aplicacion(datos):
    datos_encapsulados = f'APLICACION({datos})'
    print("Aplicación envía:", datos_encapsulados)
    return capa_presentacion(datos_encapsulados)

def capa_presentacion(datos):
    datos_encapsulados = f'PRESENTACION({datos})'
    print("Presentación envía:", datos_encapsulados)
    return capa_sesion(datos_encapsulados)

def capa_sesion(datos):
    datos_encapsulados = f'SESION({datos})'
    print("Sesión envía:", datos_encapsulados)
    return capa_transporte(datos_encapsulados)

def capa_transporte(datos):
    datos_encapsulados = f'TRANSPORTE({datos})'
    print("Transporte envía:", datos_encapsulados)
    return capa_red(datos_encapsulados)

def capa_red(datos):
    datos_encapsulados = f'RED({datos})'
    print("Red envía:", datos_encapsulados)
    return capa_enlace(datos_encapsulados)

def capa_enlace(datos):
    datos_encapsulados = f'ENLACE({datos})'
    print("Enlace envía:", datos_encapsulados)
    return capa_fisica(datos_encapsulados)

def capa_fisica(datos):
    datos_encapsulados = f'FISICA({datos})'
    print("Física envía:", datos_encapsulados)
    return datos_encapsulados
```

Paso 2: Simular el proceso de desencapsulación.

Ahora necesitamos un conjunto de funciones para desencapsular los datos, que se activarán en el punto de recepción.

```bash
def desencapsular_fisica(datos):
    return datos[7:-1]

def desencapsular_enlace(datos):
    return desencapsular_fisica(datos[6:-1])

def desencapsular_red(datos):
    return desencapsular_enlace(datos[4:-1])

def desencapsular_transporte(datos):
    return desencapsular_red(datos[11:-1])

def desencapsular_sesion(datos):
    return desencapsular_transporte(datos[7:-1])

def desencapsular_presentacion(datos):
    return desencapsular_sesion(datos[14:-1])

def desencapsular_aplicacion(datos):
    return desencapsular_presentacion(datos[11:-1])
```

Paso 3: Demostración del proceso completo.

```bash
def demostracion():
    mensaje_original = "Hola Hola"
    print("Mensaje original:", mensaje_original)
    
    datos_encapsulados = capa_aplicacion(mensaje_original)
    print("Datos encapsulados:", datos_encapsulados)
    
    datos_desencapsulados = desencapsular_aplicacion(datos_encapsulados)
    print("Datos desencapsulados:", datos_desencapsulados)
    
if __name__ == "__main__":
    demostracion()
```

### Ejercicios adicionales para extender el uso
+ Implementa un mecanismo para manejar errores en cada capa.
+ Simula más detalles de cadad capa, por ejemplo, manejar la segmentación en la capa de transporte o las direcciones IP en la capa de red.
+ Utiza estás funciones en combinación con sockets para enviar y recibir datos a través de una red real, manteniendo la simulación de encapsulación y desencapsulación.

Mi respuesta:

```bash
```