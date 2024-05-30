# Evidencias del desarrollo del presente laboratorio:

En este laboratorio, se creará una alarma de Amazon CloudWatch que notifica cuando la cuenta haya gastado más de una determinada cantidad de dinero. La alarma envía un mensaje a Amazon Simple Notification Service (Amazon SNS) para que envíe una notificación por correo electrónico o mensaje de texto.

### **Palabras clave:**

**- Tema:** Actúa como un canal de comunicación donde se puede publicar mensajes de alerta y eventos.

**- FIFO (first in, first out; primero en entrar, primero en salir):** Guarda analogía con las personas que esperan en una cola y son atendidas en el orden en la que llegaron.

**- Protocolo:** Se refiere al tipo de punto de enlace (correo electrónico, SMS).

---
### **Pasos:**
+ Accedemos a la consola de administración de AWS:

![alt text](image.png)

+ Elegimos el servicio Simple Notification Service:

![alt text](image-1.png)

+ Presionamos en temas en el panel de navegación izquierdo:

![alt text](image-2.png)

+ Damos en crear un tema:

![alt text](image-3.png)

+ Seleccionamos el tipo estandar e introducimos un nombre:

![alt text](image-4.png)

+ Y damos en crear un tema:

![alt text](image-5.png)

+ Ahora vamos a suscribirnos para que, cuando se publique un mensaje en el tema, se envíe una notificación al teléfono o correo electrónico:

![alt text](image-6.png)

+ Elegiremos el tipo de enlace como correo electrónico:

![alt text](image-7.png)

+ Damos en crear una suscripción:

![alt text](image-8.png)

+ Confirmamos la suscripción ingresando al mensaje en la bandeja de entrada:

![alt text](image-9.png)

+ Comprobamos la suscripción:

![alt text](image-10.png)

+ Ahora, crearemos una alarma de CloudWatch seleccionandolo en el panel izquierdo de servicios:

![alt text](image-11.png)

+ Ahora damos en crear alarma:

![alt text](image-12.png)

+ Damos en seleccionar una métrica y a continuación en facturación:

![alt text](image-13.png)

+ Ahora en cargo total estimado:

![alt text](image-14.png)

+ Marcamos la casilla y seleccionar una métrica:

![alt text](image-15.png)

+ Ahora vamos a configurarlo:

![alt text](image-16.png)

+ Damos en siguientey configuramos las acciones:

![alt text](image-17.png)

+ Click en siguiente para agregar el nombre y descripción de la alarma:

![alt text](image-18.png)

+ Comprobamos las configuraciones:

![alt text](image-19.png)

+ Y damos en crear alarma:

![alt text](image-20.png)

+ Se creó correctamente la alarma:

![alt text](image-21.png)
![alt text](image-22.png)

### 🧑‍💻¡LABORATORIO COMPLETADO!🧑‍💻