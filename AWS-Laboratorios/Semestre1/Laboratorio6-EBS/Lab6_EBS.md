# Evidencias del desarrollo del presente laboratorio:

En este laboratorio, se creará una instancia de Amazon Elastic Compute Cloud y, a continuación, se adjuntará un volumen de Amazon Elastic Block Store.

### **Palabras clave:**
**- A:** A

---
### **Pasos:**
+ Accedemos a la consola de administración de AWS:
![alt text](image.png)

+ Lanzaremos una instancia EC2 como la hemos estado conociendo:
![alt text](image-1.png)

+ Lo que sigue es adjuntar un volumen de EBS a la instancia de EC2.
+ Visualizamos nuestra instancia:

![alt text](image-2.png)

+ Ahora tomaremos nota de la zona de disponibilidad en la opción redes, esto porque el volumen de EBS debe estar en la misma zona de disponibilidad que tu instancia:

![alt text](image-3.png)

+ Ahora, en el panel izquierdo, damos click en volúmenes dentro de Elastic Block Store:

![alt text](image-4.png)

+ Damos en crear volumen:

![alt text](image-5.png)

+ Crearemos un volumen de 1 GiB asegurando que se encuentra en la misma zona de disponibilidad:

![alt text](image-6.png)

+ Presionamos crear volumen y se mostrará un mensaje de confirmación:

![alt text](image-7.png)

+ Hacemos click en el nuevo volumen y en acciones damos en asociar volumen: 

![alt text](image-8.png)

+ Seleccionamos la instancia EC2 creada inicialmente:

![alt text](image-9.png)

+ Damos en asociar volumen y mostrará el mensaje de proceso satisfactorio:

![alt text](image-10.png)

### 🧑‍💻¡LABORATORIO COMPLETADO!🧑‍💻