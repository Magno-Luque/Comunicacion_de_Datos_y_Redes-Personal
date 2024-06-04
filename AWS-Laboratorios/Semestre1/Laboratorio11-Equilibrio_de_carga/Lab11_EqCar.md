# Evidencias del desarrollo del presente laboratorio:

En este laboratorio, se creará y configurará un balanceador de carga, registrar una página web como destino del balanceador de carga y probar el balanceador de carga.

### **Palabras clave:**

**- Política:** Define qué acciones están permitidas o denegadas para recursos concretos de AWS.

---
### **Pasos:**
+ Accedemos a la consola de administración de AWS:

![alt text](image.png)

+ Se lanzará una instancia de Amazon EC2 como lo hemos estado haciendo pero con un paso adicional.
+ En configuraciones de red, específicamente en el botón desplegable Subred, seleccionar "Zona de disponibilidad us-east-1a":

![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

+ Accedemos al sitio web de la instancia de EC2:

![alt text](image-4.png)

+ Se crea una segunda instancia EC2 para el balanceo de carga, lo haremos replicando la primera instancia como se muestra a continuación: 

![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)

+ Comprobamos que se lanzó correctamente las dos instancias EC2:

![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)

+ Ahora crearemos los balanceadores de carga:

![alt text](image-12.png)

+ Damos en crear balanceador de carga con el tipo de equilibrio "Balanceador de carga de aplicaciones":

![alt text](image-13.png)

+ Agregamos el nombre:

![alt text](image-14.png)

+ Ahora seleccionamos las dos zonas de disponibilidad en donde lanzamos las instancias:

![alt text](image-15.png)

+ Configuramos el grupo de seguridad:

![alt text](image-16.png)

+ Damos click en "crear grupo de destino" y agregamos el nombre del grupo de destino:

![alt text](image-17.png)

+ Completamos comprobaciones de estado:

![alt text](image-18.png)

+ Damos en siguiente y seleccionamos las instancias que acabamos de crear:

![alt text](image-19.png)

+ Incluimos como pendiente a continuación:

![alt text](image-20.png)

+ Y seleccionamos en crear grupo de destino:

![alt text](image-21.png)

+ Ahora, en el botón desplegable tomamos al grupo de destino que acabamos de crear: 

![alt text](image-22.png)

+ Nos dirigimos a la parte inferior de la página y creamos el balanceador de carga:

![alt text](image-23.png)

+ Esperamos hasta que el estado del balanceador esté activo:

![alt text](image-24.png)

+ Ahora vamos a probar el balanceador de carga.
+ Copiamos el nombre DNS en el navegador web:

Podemos notar que el mensaje que muestra cambia varias veces, esto significa que el balanceador de carga lo ha dirigido al servidor web de la otra instancia de EC2 que se creó.

![alt text](image-25.png)
![alt text](image-26.png)

### 🧑‍💻¡LABORATORIO COMPLETADO!🧑‍💻