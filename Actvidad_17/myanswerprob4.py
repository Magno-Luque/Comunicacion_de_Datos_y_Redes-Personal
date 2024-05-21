# Definimos las funciones de cada capa
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


# Definimos las funciones que desencapsulan los datos
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


# Definimos la función de demostración
def demostracion():
    mensaje_original = "Hola Hola"
    print("Mensaje original:", mensaje_original)
    
    datos_encapsulados = capa_aplicacion(mensaje_original)
    print("Datos encapsulados:", datos_encapsulados)
    
    datos_desencapsulados = desencapsular_aplicacion(datos_encapsulados)
    print("Datos desencapsulados:", datos_desencapsulados)
    
if __name__ == "__main__":
    demostracion()