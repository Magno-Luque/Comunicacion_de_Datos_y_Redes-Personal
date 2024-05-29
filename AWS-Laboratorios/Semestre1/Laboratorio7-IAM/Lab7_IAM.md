# Evidencias del desarrollo del presente laboratorio:

En este laboratorio, se explorarán a los usuarios, los grupos y las políticas del servicio AWS Identity and Access Management (IAM).

### **Palabras clave:**

**- Política:** Define qué acciones están permitidas o denegadas para recursos concretos de AWS.

---
### **Pasos:**
+ Accedemos a la consola de administración de AWS:
![alt text](image.png)

+ Seleccionamos el IAM como servicio en donde ya estarán generadas los usuarios de IAM:
![alt text](image-1.png)
![alt text](image-2.png)

+ Seleccionamos al usuario 1 (inicialmente sin permisos, no pertenece a ningún grupo y con sus credenciales): 
![alt text](image-3.png)

+ Visualizamos también a los grupos de usuarios:
![alt text](image-4.png)

+ Seleccionamos al grupo S3-Support:
![alt text](image-5.png)

+ Este grupo está asociada a una política:
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)

+ Así para los demás grupos, cada uno con disintas políticas.

+ Ahora pasaremos a un escenario empresarial:

1. Asignaremos a los usuarios a sus grupos como indica en la siguiente tabla:
![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-13.png)
![alt text](image-14.png)
![alt text](image-15.png)
![alt text](image-16.png)
![alt text](image-17.png)
![alt text](image-18.png)

+ Cada usuario ya fue asignado a cada grupo:
![alt text](image-19.png)

+ Ahora vamos a iniciar sesión con las credenciales de cada uno de los usuarios:
![alt text](image-20.png)

1. user-1 (posee permisos para ver la lista de los buckets de Amazon S3 y su contenido; mas no de obsevar siquiera las instancias EC2):
![alt text](image-21.png)
![alt text](image-22.png)
![alt text](image-23.png)
![alt text](image-24.png)

2. user-2 (posee permisos para solamente visualizar las instancias EC2):
![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)
![alt text](image-28.png)
![alt text](image-29.png)
![alt text](image-30.png)

3. user-3 (permisos de detener instancias EC2):
![alt text](image-31.png)
![alt text](image-32.png)
![alt text](image-33.png)

### 🧑‍💻¡LABORATORIO COMPLETADO!🧑‍💻