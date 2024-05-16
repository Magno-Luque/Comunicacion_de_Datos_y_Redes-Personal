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