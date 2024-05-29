# Evidencias del desarrollo del presente laboratorio:

En este laboratorio se usará Amazon CloudFront como red de entrega de contenido (CDN) para un sitio web almacenado en Amazon S3.

### **Palabras clave:**
**- AWS CLI:** Es una interfaz de línea de comandos que permite interactuar con los servicios de AWS.

---
### **Pasos:**
+ Accedemos a la consola de administración de AWS:
![alt text](image.png)

+ Creamos el bucket:
![alt text](image-1.png)
![alt text](image-2.png)

+ Añadimos una política al bucket creado:
![alt text](image-3.png)

+ Desbloqueamos para el acceso al público:
![alt text](image-4.png)
![alt text](image-5.png)

+ Editamos las propiedades del objeto:
![alt text](image-6.png)
![alt text](image-7.png)

+ Editamos las políticas del bucket:
![alt text](image-8.png)
![alt text](image-9.png)

+ Cargaremos el archivo HTML:
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)

+ Habilitamos el alojamiento de sitios web estáticos en propiedades del bucket:
![alt text](image-13.png)

+ Ahora nos dirigimos al punto de enlace de sitio web del bucket:
![alt text](image-14.png)
![alt text](image-15.png)

+ Ahora vamos a crear la distribución de CloudFront para servir al sitio web:
![alt text](image-16.png)
![alt text](image-17.png)
![alt text](image-18.png)
![alt text](image-19.png)
![alt text](image-20.png)

+ Creamos la distribución:
![alt text](image-21.png)

+ Cargamos un archivo de imagen el el bucket otorgando el permiso al público:
![alt text](image-22.png)

+ Creamos un nuevo archivo HTML con las siguientes especificaciones:
```bash
<html>
    <head>My CloudFront Test</head>
    <body>
        <p>My test content goes here.</p>
        <p><img src="http://domain-name/object-name" alt="my test image">
    </body>
</html>
```
1. El domain-name es el nombre de dominio para la distribución de CloudFront.
2. Objet-name es el nombre del archivo de imagen,

La línea de código editadad debe ser similar a:
```bash 
<p><img src="http://d2f1zrxb2zaf30.cloudfront.net/picture.jpg" alt="my test image">
```

+ Y abrimos el archivo editado en el navegador de internet:
![alt text](image-23.png)

### 🧑‍💻¡LABORATORIO COMPLETADO!🧑‍💻