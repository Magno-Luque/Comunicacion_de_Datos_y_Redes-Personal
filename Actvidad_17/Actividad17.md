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