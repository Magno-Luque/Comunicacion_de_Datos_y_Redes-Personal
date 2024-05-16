# Definimos la función servidor.
def servidor(mensaje):
    """Procesa los mensajes enviados por el cliente según el comando especificado."""
    comando, _, contenido = mensaje.partition(':')
    if comando.strip().lower() == 'eco':
        return contenido.strip()
    elif comando.strip().lower() == 'reverso':
        return contenido.strip()[::-1]
    else:
        return "Comando no reconocido."
    
# Definimos la función cliente.
def cliente(mensaje):
    """Enviar los mensajes al servidor y procesar la respuesta."""
    respuesta = servidor(mensaje)
    print(f'Servidor dice: {respuesta}')
    
# Definimos la función que permite llamar a la función cliente con diferentes mensajes.
def main():
    cliente("eco: Hola Mundo")
    cliente("reverso: Hola Mundo")
    cliente("sumar: 123 + 456")
    
if __name__ == "__main__":
    main()