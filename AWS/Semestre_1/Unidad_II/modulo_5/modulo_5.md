## Módulo 5: Entrega de contenido

**Finalidad del módulo:** 

Obtener información sobre la red de entrega de contenido (CDN: Content Delivery Network), Amazon CloudFront.

**Descripción del módulo:**

Importancia de las ubicaciones de borde y el almacenamiento en caché para una CDN. Creación de una distribución de CloudFront y adjuntarlo a un bucket en Amazon S3 que contiene un archivo web HTML.

**Teminología tecnológica:**

**- Amazon CloudFront:** Es un servicio de red de entrega de contenido (CDN) rápida que entrega datos, videos, aplicaciones e interfaces de programación de aplicaciones(API) de forma segura, con baja latencia (tiempo que tarda un paquete de datos viajar desde su origen hacia su destino) y altas velocidades de transferencia (cantidad de datos), todo ello dentro de un entorno favorable para los desarrolladores. 

**- AWS Direct Content:** Permite establecer una conectividad privada entre AWS y su centro de datos, oficina o entorno de coubicación, lo que en muchos casos puede reducir los costos de red, aumenta el rendimiento del ancho de banda (capacidad máxima teórica de una conexión de red) y ofrecer una experiencia de red más uniforme.

**- Almacenamiento en caché:** Almacena los datos que son solicitados con frecuencia en ubicaciones más cercanas al usuario o al dispositivo que lo solicita, en este caso en ubicaciones de borde (puntos estratégicos de una red que gestiona el tráfico entre una red local y redes externas) para que se pueda acceder a ellos rápidamente. 

**- Red de entrega de contenido (CDN):** Es un sistema de servidores distribuidos (red) que entrega páginas y otros contenidos web a un usuario, en función de la ubicación geográfica del usuario.  

**- Distribución:** Indica a CloudFront dónde obtener la iformación que está almacenado en caché en las ubicaciones de borde y administrar la entrega de contenido. 

**- Ubicación de borde:** Sitios en el que se pueden almacenar los datos para reducir la latencia. A menudo, las ubicaciones de borde estarán cerca de las zonas de gran población que generarán grandes volúmenes de tráfico. (TTL: Time to Live)

**- Origen:** Describe el bucket de Amazon S3, el servidor de Protocolos de Transferencia de Hipertexto (servidor web) u otro servidor del que CloudFront obtiene sus archivos. 