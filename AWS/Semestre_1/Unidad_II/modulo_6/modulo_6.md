## Módulo 6: Almacenamiento virtual

**Finalidad del módulo:** 

Recibir információn general de Amazon Elastic Block Store (Amazon EBS). Comparar Amazon EBS y Amazon S3. Aprender sobre los distintos niveles de almacenamiento. 

**Descripción del módulo:**

Examinar las ventajas y características de Amazon EBS. Creación de los volúmenes de EBS y se adjuntará a una instancia de Amazon EC2.

**Teminología tecnológica:**

**- Amazon Elastic Block Store (Amazon EBS):** Permite el almacenamiento para instancias específicas de Amazon EC2. Considerado como la unidad de almacenamiento de la instancia EC2. 

**- AWS Elastic Compute Cloud (Amazon EC2):** Servicio web que ofrece capacidad informática escalable en la nube.  Considerado como alquilar una computadora en la nube. 

**- Unidad de disco duro (HDD: Hard Disk Drive):** Almacenamiento más lento que utiliza un disco giratorio para almacenar datos.

**- Operaciones de entrada y salida por segundo (IOPS):** Medida de rendimiento frecuente que se utiliza para comparar dispositivos de almacenamiento informático como HDD y SSD. 

**- Unidad de estado sólido (SSD: Solid State Drive):** Almacenamiento muy rápido que utiliza memoria flash en lugar de un disco giratorio. 

**- Amazon S3 Glacier:** Es rentable y altamente duradera para el almacenamiento de datos a largo plazo en la nube.

---
Sistemas de archivos de nueva tecnología (NTFS: New Technology File System).

Tabla de asignación de archivos (FAT: File Allocation Table).

---
A continuación, se presenta algunas diferencias entre el almacenamiento de datos de Amazon S3 y Amazon EBS:

+ Amazon EBS  solo se puede utilizar cuando se adjunta a una instancia EC2. En cambio, se puede acceder a Amazon S3 de manera independiente mediante los protocolos de HTTP.

+ Amazon EBS no puede contener tantos datos como Amazon S3.

+ Amazon EBS no puede adjuntarse a una instancia EC2, mientras que varias instancias EC2 pueden acceder a los datos de un bucket de S3. 

+ Amazon S3 presenta más demoras que Amazon EBS a la hora de escribir datos. 

+ Amazon EBS incluye tres tipos de volúmenes (volúmenes en estado sólido (SSD), volúmenes de unidades de estadi sólido (HDD), volúmenes de generaciones anteriores), mientras que Amazon incluye más tipos.