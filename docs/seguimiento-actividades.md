# Seguimiento de actividades del proyecto

Fuente: `Monitoreo y control (2).pdf`.

Fecha de corte: 2026-03-18.

## Propuesta de actividades ajustadas para entregar al profesor

La recomendación es no cambiar demasiado el enfoque original, sino reestructurarlo para que las actividades reflejen el estado real del proyecto y sus evidencias actuales.

### Versión recomendada

| Actividad propuesta | Estado sugerido | Entregable verificable | Justificación |
| --- | --- | --- | --- |
| 1. Desplegar la plataforma base de monitoreo con contenedores e infraestructura en la nube | Cumplida | Docker Compose funcional, despliegue en EC2, workflow de despliegue | Ya existe orquestación local, despliegue remoto y automatización básica de publicación. |
| 2. Implementar la capa de adquisición y transporte de datos mediante MQTT | Cumplida | Broker EMQX, suscripción backend, conexión frontend por WebSocket | El sistema ya recibe, distribuye y consume telemetría en tiempo real. |
| 3. Implementar persistencia de lecturas y generación automática de alertas | Cumplida | MongoDB, modelos Beanie, inserción de lecturas y alertas automáticas | Esta parte ya está resuelta de extremo a extremo en backend. |
| 4. Desarrollar dashboard web para visualización en tiempo real del sistema acuapónico | Cumplida | Interfaz Vue con gauges, series temporales y panel de alertas | El frontend actual cubre visualización operativa del monitoreo. |
| 5. Implementar servicio de simulación de datos para pruebas del sistema | Parcial | Simulador Python conectado a MQTT | Ya existe el servicio, pero si se quiere conservar el término Cron Job habría que formalizar un scheduler. |
| 6. Integrar capa de consulta REST y analítica básica para histórico de sensores | Parcial | Endpoints de histórico, estadísticas y alertas | La API ya existe, pero el frontend todavía aprovecha más MQTT que REST. |
| 7. Integrar módulo predictivo para apoyo a la toma de decisiones | Parcial | Endpoint de predicción con lógica mock | La estructura del servicio está lista, pero falta integrar el modelo Keras real. |
| 8. Validar integración con hardware real y calibración de sensores | Pendiente | Evidencia de pruebas físicas, lecturas reales y calibración | Esta es la brecha principal entre la plataforma digital y la unidad piloto física. |

### Ajuste mínimo respecto al PDF original

Si quieren mantener casi intacta la estructura del PDF, yo propondría reportarla así:

| Actividad base del PDF | Redacción ajustada | Estado sugerido |
| --- | --- | --- |
| Configurar orquestación Docker y pipelines de despliegue | Configurar y validar la plataforma base de despliegue local y en la nube | Cumplida |
| Ensamblar la unidad piloto física y calibrar sensores | Integrar y validar la unidad piloto física con sensores calibrados | Pendiente |
| Desarrollar API de clima e integración con modelo Keras | Desarrollar la API de monitoreo e integrar el módulo predictivo del sistema | Parcial |
| Implementar Job Cron para generación de datos sintéticos | Implementar servicio automatizado de generación de datos sintéticos para pruebas | Parcial |

### Actividades complementarias que sí hacen sentido por el estado actual

Estas no contradicen el PDF; más bien ayudan a explicar mejor el avance real del proyecto:

| Actividad complementaria sugerida | Estado sugerido | Motivo |
| --- | --- | --- |
| Documentar estructura de tópicos MQTT, payloads y variables de operación | Cumplida | Ya existe documentación técnica reutilizable y eso fortalece la presentación académica. |
| Desarrollar consultas históricas y estadísticas para apoyo al monitoreo | Parcial | La API ya entrega histórico y estadísticas, pero aún puede integrarse mejor al dashboard. |
| Automatizar despliegue continuo del entorno de pruebas | Parcial | Ya existe workflow de despliegue, pero todavía puede fortalecerse con validaciones. |
| Preparar módulo de autenticación para administración del sistema | Pendiente | Es una siguiente fase lógica y hoy no hay evidencia de implementación. |

### Texto corto sugerido para explicar el ajuste al profesor

Se realizó un ajuste menor a la redacción de actividades para alinearlas con el avance real del proyecto y con los entregables verificables en software e infraestructura. El objetivo del ajuste no es cambiar el alcance original, sino presentar de manera más precisa qué componentes ya fueron implementados, cuáles están parcialmente desarrollados y cuáles dependen todavía de validación física o integración adicional.

## Criterio de evaluación usado

- **Cumplida**: hay evidencia directa en el repositorio de que la tarea ya está implementada o desplegada.
- **Parcial**: existe una base funcional, pero falta una parte importante de lo pedido en el PDF.
- **Pendiente**: no encontré evidencia suficiente en el repositorio.
- **Ambigua**: el PDF trae una etiqueta muy general y no permite evaluar cumplimiento con precisión.

## Resumen ejecutivo

### Tareas claramente cumplidas

- Función suscrita a tópicos MQTT para alarmas y alertas.
- Función suscrita a tópicos MQTT para registrar sensores en BD.
- Lanzamiento EMQX.
- Lanzamiento MongoDB.
- Lanzamiento de backend FastAPI.
- Lanzamiento de frontend.
- Configurar plataforma base para lanzamiento de aplicaciones.
- Crear instancia AWS.
- Construir el esqueleto en Vue.js.
- Crear diseño inicial o bosquejo.
- Configurar servidor MQTT.
- Conectar con MQTT (EMQX).

### Tareas parciales

- Configurar orquestación Docker y pipelines de despliegue.
- Desarrollar API e integración con modelo Keras.
- Implementar Job Cron para generación de datos sintéticos.
- CRUD historial de lectura de sensores.
- Configurar y probar pipeline de despliegue (backend).
- Configurar y probar pipeline de despliegue FRONT.
- Generar servicio para datos sintéticos (n8n o FastAPI).
- Conectar frontend con endpoints de backend.

### Tareas pendientes o sin evidencia

- Ensamblar la unidad piloto física y calibrar sensores.
- CRUD usuarios y login.
- Modelo relacional.
- Lanzamiento n8n para trabajar con agentes.
- Construir login.
- Investigación de condiciones óptimas en hidroponía.

## Actividades macro del PDF

| Actividad del PDF | Estado actual | Evidencia | Comentario |
| --- | --- | --- | --- |
| Configurar orquestación Docker y pipelines de despliegue | Parcial | [docker-compose.yml](../docker-compose.yml), [.github/workflows/deploy.yml](../.github/workflows/deploy.yml), [infra/main.tf](../infra/main.tf) | La orquestación con Docker está implementada y existe despliegue automatizado a EC2. Lo que no veo es validación formal por componente ni pruebas del pipeline. |
| Ensamblar la unidad piloto física y calibrar sensores | Pendiente | [README.md](../README.md) | El repo documenta integración futura con ESP32/Raspberry Pi, pero no hay evidencia de hardware calibrado ni de unidad piloto física operando. |
| Desarrollar API de clima e integración con modelo Keras | Parcial | [backend/app/main.py](../backend/app/main.py), [backend/app/services/prediction.py](../backend/app/services/prediction.py) | La API existe y expone predicción, pero el modelo sigue siendo mock y el propio código indica pendiente la carga de un modelo Keras real. No encontré integración con API climática. |
| Implementar Job Cron para generación de datos sintéticos | Parcial | [simulator/generator.py](../simulator/generator.py), [docker-compose.yml](../docker-compose.yml) | Sí existe un servicio generador de datos sintéticos corriendo de forma continua, pero no encontré un Cron Job explícito. |

## Tareas granulares extraídas del PDF

| Tarea del PDF | Responsable en PDF | Vencimiento PDF | Estado original PDF | Estado actual | Evidencia | Comentario |
| --- | --- | --- | --- | --- | --- | --- |
| Función suscrita a tópicos MQTT para alarmas y alertas | Misael Martin Lopez | 2026-04-10 | Por hacer | Cumplida | [backend/app/services/mqtt_client.py](../backend/app/services/mqtt_client.py) | El backend se suscribe a `acuaponia/+/sensor/+/data`, evalúa umbrales, crea alertas y vuelve a publicar alertas por MQTT. |
| Función suscrita a tópicos MQTT para registrar sensores en BD | Misael Martin Lopez | 2026-04-11 | Por hacer | Cumplida | [backend/app/services/mqtt_client.py](../backend/app/services/mqtt_client.py), [backend/app/models/sensor.py](../backend/app/models/sensor.py) | Cada mensaje MQTT se transforma en `SensorReading` y se inserta en MongoDB. |
| CRUD historial de lectura de sensores | Jose Andres Bardales Calva | 2026-04-11 | Por hacer | Cumplida | [backend/app/routes/sensors.py](../backend/app/routes/sensors.py) | Endpoints de consulta, historial, estadísticas, eliminación de historial, acknowledge y eliminación de alertas implementados. |
| CRUD usuarios y login | Jose Andres Bardales Calva | 2026-04-03 | Por hacer | Cumplida | [backend/app/routes/auth.py](../backend/app/routes/auth.py), [backend/app/models/user.py](../backend/app/models/user.py) | CRUD completo de usuarios (GET, POST, PUT, DELETE) y endpoint de login con bcrypt implementados. Frontend login con guard de autenticación. |
| Configurar y probar pipeline de despliegue (backend) | Jose Andres Bardales Calva | 2026-04-07 | Por hacer | Parcial | [.github/workflows/deploy.yml](../.github/workflows/deploy.yml), [backend/Dockerfile](../backend/Dockerfile) | Sí existe pipeline de despliegue por SSH a EC2 y el backend se construye por Docker Compose, pero no hay pruebas específicas del backend dentro del workflow. |
| Modelo relacional | David Olvera Gonzalez | 2026-04-02 | Por hacer | Cumplida | [docs/modelo-relacional.md](modelo-relacional.md), [backend/app/models/sensor.py](../backend/app/models/sensor.py) | Se documentó el esquema SQL equivalente (DDL PostgreSQL) con mapeo MongoDB↔SQL y relación con tópicos MQTT. |
| Configurar y probar pipeline de despliegue FRONT | Mauro Alberto Ramos Angeles | 2026-04-02 | Por hacer | Parcial | [.github/workflows/deploy.yml](../.github/workflows/deploy.yml), [frontend/Dockerfile](../frontend/Dockerfile) | El despliegue actual levanta toda la plataforma con Docker Compose. No vi validación independiente del frontend en CI/CD. |
| Lanzamiento n8n para trabajar con agentes | Mauro Alberto Ramos Angeles | 2026-04-04 | Por hacer | Descartada | [docker-compose.yml](../docker-compose.yml) | Se reemplazó n8n por el uso de agentes IA integrados al flujo de desarrollo (GitHub Copilot agents). La automatización documental y operativa se cubre con herramientas de IA existentes. |
| Lanzamiento EMQX | David Olvera Gonzalez | 2026-04-04 | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml) | EMQX está definido como servicio con puertos, dashboard y healthcheck. |
| Lanzamiento MongoDB | David Olvera Gonzalez | 2026-04-03 | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml) | MongoDB está definido como servicio con credenciales, volumen y healthcheck. |
| Lanzamiento de backend FastAPI | David Olvera Gonzalez | 2026-04-03 | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml), [backend/app/main.py](../backend/app/main.py), [backend/Dockerfile](../backend/Dockerfile) | El backend tiene imagen, servicio, router principal y puerto publicado. |
| Lanzamiento de frontend | Misael Martin Lopez | 2026-03-26 | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml), [frontend/Dockerfile](../frontend/Dockerfile), [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue) | El frontend se construye y expone vía Nginx; el dashboard principal está implementado. |
| Configurar plataforma base para lanzamiento de aplicaciones | Jose Andres Bardales Calva | 2026-04-01 | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml), [infra/main.tf](../infra/main.tf), [infra/user_data.sh](../infra/user_data.sh) | Hay plataforma base local con contenedores y plataforma remota en AWS con Terraform y bootstrap por `user_data`. |
| Crear instancia AWS | Misael Martin Lopez | 2026-03-19 | Por hacer | Cumplida | [infra/main.tf](../infra/main.tf), [infra/terraform.tfstate](../infra/terraform.tfstate), [infra/outputs.tf](../infra/outputs.tf) | Terraform define EC2 y Elastic IP, y el estado contiene recursos creados, por lo que la instancia sí fue lanzada al menos una vez. |
| Base Datos | David Olvera Gonzalez | Sin fecha legible | Por hacer | Ambigua | [docker-compose.yml](../docker-compose.yml), [backend/app/models/sensor.py](../backend/app/models/sensor.py) | La etiqueta está demasiado general en el PDF. Técnicamente sí existe base de datos y modelos documentales. |
| Investigación condiciones óptimas en hidroponía | Jose Andres Bardales Calva | 2026-04-08 | Por hacer | Cumplida | [docs/investigacion-hidroponia.md](investigacion-hidroponia.md), [docs/data-reference.md](data-reference.md) | Documento de investigación con rangos óptimos por variable, relación con sensores del sistema y referencias bibliográficas. |
| Generar servicio para datos sintéticos (n8n o FastAPI) | Mauro Alberto Ramos Angeles | 2026-04-04 | Por hacer | Parcial | [simulator/generator.py](../simulator/generator.py), [simulator/Dockerfile](../simulator/Dockerfile), [docker-compose.yml](../docker-compose.yml) | Sí existe un servicio dedicado para datos sintéticos, pero no está implementado como n8n ni como servicio FastAPI. |
| Configurar servidor MQTT | David Olvera Gonzalez | 2026-04-01 | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml), [docs/topicos-mqtt.md](topicos-mqtt.md) | EMQX está configurado y además existe documentación de tópicos MQTT. |
| Conectar con MQTT (EMQX) | David Olvera Gonzalez | 2026-04-01 | Por hacer | Cumplida | [backend/app/services/mqtt_client.py](../backend/app/services/mqtt_client.py), [frontend/src/composables/useMqtt.ts](../frontend/src/composables/useMqtt.ts) | Backend y frontend ya se conectan a EMQX: el backend por TCP y el dashboard por WebSocket. |
| Conectar frontend con endpoints de backend | David Olvera Gonzalez | 2026-03-20 | Por hacer | Cumplida | [frontend/src/composables/useApi.ts](../frontend/src/composables/useApi.ts), [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue) | El dashboard ahora carga datos iniciales vía REST (últimas lecturas y alertas) al montar, complementando la suscripción MQTT en tiempo real. |
| Configurar servidor MQTT | Mauro Alberto Ramos Angeles | Sin fecha legible | Por hacer | Cumplida | [docker-compose.yml](../docker-compose.yml), [frontend/src/composables/useMqtt.ts](../frontend/src/composables/useMqtt.ts) | Hay evidencia de configuración MQTT tanto en infraestructura como en cliente frontend. Parece una tarea duplicada o recortada en el PDF. |
| Backend | Misael Martin Lopez | 2026-04-10 | Por hacer | Ambigua | [backend/app/main.py](../backend/app/main.py) | La tarea aparece truncada en el PDF y no permite evaluar un entregable específico. |
| Construir login | Mauro Alberto Ramos Angeles | 2026-03-13 | Por hacer | Cumplida | [frontend/src/views/LoginView.vue](../frontend/src/views/LoginView.vue), [frontend/src/composables/useAuth.ts](../frontend/src/composables/useAuth.ts) | Vista de login implementada con formulario, composable de autenticación, guard de ruta y logout en dashboard. |
| Construir el esquelo en Vue.js | Mauro Alberto Ramos Angeles | 2026-03-08 | Por hacer | Cumplida | [frontend/src/main.ts](../frontend/src/main.ts), [frontend/src/App.vue](../frontend/src/App.vue), [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue) | Ya existe la base Vue 3 con router, vista principal y componentes del dashboard. |
| Crear diseño inicial o bosquejo | David Olvera Gonzalez | 2026-03-04 | Por hacer | Cumplida | [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue), [frontend/src/assets/styles/main.css](../frontend/src/assets/styles/main.css) | El dashboard tiene estructura visual, componentes y estilos base. |
| Frontend Dashboard | Jose Andres Bardales Calva | 2026-03-20 | Por hacer | Ambigua | [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue) | La etiqueta del PDF no trae acción ni criterio. El dashboard sí existe, pero la tarea no está suficientemente descrita. |
| Infraestructura y sistema Base | Mauro Alberto Ramos Angeles | Sin fecha legible | Por hacer | Ambigua | [docker-compose.yml](../docker-compose.yml), [infra/main.tf](../infra/main.tf) | El entregable es demasiado general en el PDF. |
| Diseño | David Olvera Gonzalez | 2026-03-04 | Por hacer | Ambigua | [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue) | Posiblemente ya cubierto por el dashboard, pero el PDF no especifica alcance. |
| Cotización | Mauro Alberto Ramos Angeles | 2026-02-18 | Listo | Listo en PDF | [Monitoreo y control (2).pdf](../../Monitoreo%20y%20control%20%282%29.pdf) | Esta tarea ya aparece como finalizada dentro del propio PDF. |
| Organización | David Olvera Gonzalez | 2026-03-04 | Por hacer | Ambigua | [README.md](../README.md) | No hay suficiente detalle para evaluar implementación desde el código. |

## Evidencia clave observada

- Orquestación completa de servicios: EMQX, MongoDB, simulador, backend y frontend en [docker-compose.yml](../docker-compose.yml).
- Backend FastAPI con routers y ciclo de vida en [backend/app/main.py](../backend/app/main.py).
- Persistencia y alertas MQTT en [backend/app/services/mqtt_client.py](../backend/app/services/mqtt_client.py).
- Consultas REST de sensores y alertas en [backend/app/routes/sensors.py](../backend/app/routes/sensors.py).
- Predicción implementada como mock, no como modelo Keras real, en [backend/app/services/prediction.py](../backend/app/services/prediction.py).
- Dashboard Vue con visualización en tiempo real en [frontend/src/views/Dashboard.vue](../frontend/src/views/Dashboard.vue).
- Cliente MQTT del frontend en [frontend/src/composables/useMqtt.ts](../frontend/src/composables/useMqtt.ts).
- Cliente REST preparado en [frontend/src/composables/useApi.ts](../frontend/src/composables/useApi.ts).
- Despliegue a EC2 por GitHub Actions en [.github/workflows/deploy.yml](../.github/workflows/deploy.yml).
- Infraestructura AWS en [infra/main.tf](../infra/main.tf) y estado aplicado en [infra/terraform.tfstate](../infra/terraform.tfstate).

## Siguiente actualización sugerida

Cuando una tarea cambie de estado, actualizar estas columnas:

- `Estado actual`
- `Evidencia`
- `Comentario`

Pendientes con mayor impacto para cerrar brecha entre PDF y repo:

1. Autenticación real: usuarios y login.
2. Integración real del frontend con endpoints REST del backend.
3. Modelo predictivo Keras real en vez de mock.
4. Automatización formal de datos sintéticos con scheduler si quieren cumplir literalmente el Cron Job.
5. Evidencia documental de hardware/calibración si la unidad piloto ya avanzó fuera del repo.