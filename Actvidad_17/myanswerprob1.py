# Importamos librerías
import re  # módulo que proporciona operaciones de coincidencia
import random as rd

# Modificación de funciones 
def servidor(mensaje):
    """Procesa los mensajes enviados por el cliente según el comando especificado."""
    mensaje = mensaje.upper()  
    if re.match("^[A-Z:0-9\s+]+$",mensaje):
        comando, _, contenido = mensaje.partition(':')
        
        if comando.strip() == 'ECO':
            return contenido.strip()
        elif comando.strip() == 'REVERSO':
            return contenido.strip()[::-1]
        elif comando.strip() == 'SUMAR':
            numeros = [int(i) for i in contenido.split('+')]
            suma = sum(numeros)
            return suma
        else:
            return "Comando no reconocido."
    else:
        return "El mensaje contiene caracteres no permitidos."
    
def cliente(mensaje):
    """Enviar los mensajes al servidor y procesar la respuesta."""
    respuesta = servidor(mensaje)
    print(f'Servidor dice: {respuesta}')
    
def main():
    cliente("eco: Hola Mundo")
    cliente("reverso: Hola Mundo")
    cliente("sumar: 123 + 456")
    cliente("sumar: @")
    
if __name__ == "__main__":
    main()