## Módulo 7: Seguridad I

**Finalidad del módulo:** 

Se obtendrá información general sobre la seguridad en la nube en relación con *AWS Identity and Access Management* (IAM). A esto se incluye información sobre las prácticas recomendadas, los roles, los usuarios, las políticas y los grupos de seguridad.

**Teminología tecnológica:**

**- Amazon Identity Access Management (Amazon IAM):** Se trata de aplicar controles para los usuarios que necesitan acceder a recursos informáticos.

**- Rol:** Es una identidad de IAM que se puede crear en la cuenta y que tiene permisos específicos.

**- Usuario:** Es la entidad que se crea en AWS que representa a la persona o aplicación que la utiliza y que interactúa con AWS. Y este usuario está compuesto por un nombre y credenciales. 

**- Grupo de seguridad:** Un grupo de seguridad actúa como un firewall virtual para controlar el tráfico entrante y saliente.

**- Política:** Se trata de un objeto de AWS que, cuando se asocia a una identidad o recurso, define sus permisos. AWS es el que evalúa estas políticas cuando una entidad principal (usuario o rol) realiza una solicitud.

**- Amazon  Inspector:** Ayuda a los clientes a identificar vulnerabilidades de seguridad y las desviaciones de las prácticas recomendadas de seguridad en las aplicaciones, antes de que se implementen y mientras se ejecutan en entornos de producción. 

**- Grupo:** Un grupo de IAM es un conjunto de usuarios de IAM. Los grupos permiten especificar permisos a varios usuarios, lo que facilita la administración de permisos de dichos usuarios. 

**- Usuario raíz:** Cuando se crea una cuenta AWS por primera vez, comienza con una identidad de inicio de sesión único que tiene acceso total a todos los servicios y recursos de AWS en la cuenta.

**- Credencial:** Las credenciales de AWS verifican quién es usted y si tiene permiso para acceder a los recursos que solicita. 

**- Habilitación de Multi-Factor Authentication (MFA):** Se trata del enfoque de autenticación que requiere que se autentifiquen dos o más datos independientes.

**- Notación de objetos JavaScript (JSON):** Es la sintaxis para almacenar e intercambiar datos.

**- Multi-Factor Authentication (MFA):** Es un sistema de seguridad que requiere más de un método de autenticación de categorías independientes de credenciales para verificar la identidad del usuario para un inicio de sesión u otra transacción. 

---
El manipular información confidencial como registros bancarios y médicos en la nube, necesitan ser restringidos (quiénes pueden acceder y qué privilegios puede tener). Esto porque sitios web, bases de datos y aplicaciones son los que pueden procesarlos y almacenarlos. 

### Prácticas recomendadas de IAM

**1. Bloquee las claves de acceso de usuarios raíz de la cuenta AWS:** Proteger las claves de acceso como lo haría con los número de una tarjeta de crédito. 

**2. Cree usuarios individuales de IAM:** No utilizar las credenciales de usuario raiz de su cuenta de AWS para acceder a AWS.

**3. Utilice grupos de usuarios para asignar permisos a los usuarios de la IAM:** En lugar de definir permisos para usuarios individuales de IAM, los más conveniente es crear grupos que se relacionen con la función de su trabajo (administradores, desarrolladores, contadores, etc.). Seguidamente de definir los permisos. 

**4. Conceda menos privilegio:** Conceder solo permisos necesarios para realizar alguna tarea. Determinar los roles de los usuarios y, a continuación, crear políticas que permitan realizar solo esas tareas.

**5. Comenzar a utilizar los permisos con las políticas administradas de AWS:** Facilitan la asignación de las tareas de los permisos adecuados a los usuarios y roles.

**6. Validar políticas:** Se puede realizar la validación de políticas cuando se crea y edita políticas JSON.

**7. Usar políticas administradas por el cliente en lugar de políticas en línea:** Las políticas integradas son aquellas que solo existen en una identidad de IAM (usuario, grupo de usuario o rol). Las políticas administradas son recursos de IAM independientes que se pueden adjuntar a varias entidades.

**8. Utilizar los niveles de acceso para revisar los permisos de IAM:** Revisar periódicamente cada una de sus políticas de IAM. Asegurando que sus políticas otorgen la menor cantidad de privilegios para las acciones necesarias. 

**9. Configurar las políticas de contraseñas seguras para los usuarios:** Al permitir que los usuarios cambien sus propias contraseñas, se debe solicitar que se creen contraseñas seguras y que las cambien regularmente. 

**10. Habilitar MFA:** Los usuarios tendrán un dispositivo que generará una respuesta a un desafío de autenticación. Si la contraseña o las claves de acceso de un usuario se ven comprometidas, los recursos de la cuenta seguirán estando seguros gracias al requisito de autenticación adicional. 

**11. Utilizar roles para aplicaciones que se ejecutan en instancias de Amazon EC2:** Las aplicaciones que se ejecutan en una instancia EC2 necesitan credenciales para acceder a otros servicios de AWS. Para proporcionar credenciales a la aplicación de forma segura, utilizar roles de IAM.

**12. Utilizar roles para delegar permisos:** No hace falta compartir credenciales para permitir que los usuarios de otra cuenta de AWS acceda a los recursos de su cuenta AWS. Esto porque se pueden usar roles de IAM. 

**13. No compartir claves de acceso.**

**14. Cambiar las credenciales regularmente.**

**15. Eliminar credenciales innecesarias.** 

**16. Utilizar las condiciones de la política para obtener mayor seguridad:** Las condiciones de IAM permiten el acceso a un recurso. Por ejemplo, escribir condiciones para especificar el rango de direcciones IP. También se puede especificar que una solicitud solo se permita dentro de un intervalo de fechas o de horas. También condiciones que requieran el uso de SSL o MFT. 

**17. Supervisar la actividad de su cuenta de AWS:** Se puede usar funciones de registro de AWS. Los archivos de registro muestran la hora y la fecha de las acciones, la IP de origen de una acción y más.

