## Módulo 1: Modelos de seguridad de AWS

**Finalidad del módulo:** 

La finalidad de este módulo es proporcionar una introducción al modelo de responsabilidad compartida para la seguridad de los servicios en la nube. 


**Descripción del módulo:**

Diferenciar las responsabilidades del cliente y de AWS.

**Teminología tecnológica:**

**- Servicios en la nube:** Es el conjunto de tecnologías que almacena, procesa y permite su acceso a través de internet. 

**- Modelo de responsabilidad compartida:** Se refiere a la distribución de las responsabilidades de seguridad y cumplimiento entre AWS y el usuario. Esto quiere decir que AWS es responsable de la seguridad "de" la nube (infraestructura, software, hardware, redes y las instalaciones que ejecutan los servicios en la nube). Por otro lado, el usuario es responsable de la seguridad "en" la nube (administrar y configurar los servicios controlados por el cliente, proteger las credenciales de la cuenta y los datos del cliente).

**- Infraestructura como servicio (IaaS):** Se basa en el modelo de utilizar máquinas virtuales y servidores para que los clientes puedan alojar una amplia variedad de aplicaciones y se otorgan servicios de TI.  

**- Software como servicio (SaaS):** Otorga aplicaciones a través de internet que administra un tercero. Este tercero se refier a los usuarios finales, en donde solamente se encargan de conocer la aplicación y así poderlo administrar. 

**- Plataforma como servicio (PaaS):** Otorga entornos de ejecución para desarrollar, probar y administrar aplicaciones, se utiliza para el desarrollo de software y ofrece a los desarrolladores una plataforma para crear aplicaciones y servicios a través de internet.

**- Identity and Access Management (AMI):** Es un servicio que permite gestionar los servicios y recursos de AWS. Permite crear y administrar usuarios y grupos de AWS, y utilizar permisos para permitir y denegar su acceso a los recursos de AWS.

**- Principio de mínimo privilegio:** Se centra en el concepto de aplicar la menor cantidad de permisos a un usuario o grupo para agregar, modifcar o eliminar información.

**- Denegación de servicio (DoS):** Un atacante puede lanzar un ataque DoS contra el servicio de nube con el fin de que esta sea inaccesible y así interrumpir el servicio. Entre las diferentes formas de saturar un servicio, se tiene, hacer uso completo de la CPU, RAM, espacio de disco o ancho de banda de una red. 

**- Ataque de abrevadero:** Busca que se comprometa un grupo específico de usuarios finales al corromper sitios web visitados por estos miembros. La finalidad en sí, se trata de corromper la computadora de un usuario y obtener acceso a la red. 

**- Autenticación Multifactor (MFA):** Se trata de un sistema de seguridad que requiere más de un método de autenticación de credenciales a fin de verificar la identidad del usuario. 

---

**Complementos:**

El principio de mínimo privilegio (PoLP) se centra en el concepto de que se aplicarán la menor cantidad de permisos al usuario a fin de buscar (LEER), agregar (ESCRIBIR), eliminar (ELIMINAR), modificar (ESCRIBIR o ELIMINAR), o editar permisos para todos los usuarios y asumir la responsabilidad de todos los datos (COMPLETO). Se puede aplicar el PoLP a cada nivel de un sistema. Se aplica a usuarios finales, sistemas, procesos, redes, bases de datos, aplicaciones y cualquier otra faceta de un entorno de TI. 
