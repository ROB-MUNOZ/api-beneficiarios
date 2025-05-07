## `PROPUESTA_TECNICA.md` - Roberto Muñoz Ñanco

```markdown
# PROPUESTA TÉCNICA

## 1. Conexión segura desde API en VM Windows a SQL Server

En una arquitectura productiva donde la API se despliegue en una VM (IaaS) Windows, la conexión segura con SQL Server requiere:

- **Firewall**: Habilitar solo el puerto TCP 1433, restringido a IPs específicas.
- **Autenticación segura**: Uso de SQL Authentication o Windows Authentication con usuarios dedicados.
- **Cifrado**: Activar `Encrypt=yes` y `TrustServerCertificate=no` en el string de conexión, usando certificados válidos.
- **Red privada**: Conexión en red interna (por ejemplo, dentro de una VNet en Azure o AWS).
- **Monitoreo**: Uso de logs y métricas para detectar accesos anómalos o fallos.

La cadena de conexión se ajusta según estos parámetros y el entorno.

## 2. Simulación local sin VM

Para simular esta arquitectura, utilicé:

- SQL Server Express local
- FastAPI en entorno Python con conexión vía `pyodbc`
- Autenticación Windows (`Trusted_Connection=yes`)
- Archivo `.env` para gestionar la configuración sin exponer credenciales

Toda la lógica y conexión está contenida en `basedatos.py` y cargada desde variables de entorno.

## 3. Reflexión final

### ¿Propondrías una solución diferente?

Sí. Una opción moderna sería usar:

- **Azure SQL** (PaaS) para evitar mantenimiento de servidores
- **Azure Functions** o **AWS Lambda** para un backend sin servidor

Esto mejoraría escalabilidad, mantenimiento y costos operacionales.

### ¿Qué mecanismos actuales sugerirías?

- **GraphQL**: Mayor flexibilidad en las consultas desde frontend
- **Caching (ej. Redis)**: Reducción del tiempo de respuesta para datos repetidos
- **Serverless**: Ejecución bajo demanda según tráfico
- **OAuth2 / JWT**: Para control de acceso y seguridad API
- **CI/CD**: Automatización del despliegue usando GitHub Actions o Azure Pipelines

## Conclusión

Este proyecto demuestra cómo construí una API REST conectada a SQL Server con seguridad básica, estructura limpia y buenas prácticas de despliegue. Está diseñado para ser reproducido fácilmente en entornos locales o escalado hacia la nube.
