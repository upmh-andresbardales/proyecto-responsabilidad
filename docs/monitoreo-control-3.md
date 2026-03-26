# Universidad Politécnica Metropolitana de Hidalgo

## Carrera: Maestría en Inteligencia Artificial

### CUATRIMESTRE 2

- Grupo: Único
- Nombre del Equipo: OptiMind Four
- Docente: Dr. Víctor Darío Cuervo Pinto
- Materia: Responsabilidad Social

### Integrantes

- Bardales Calva José Andrés 253220002
- Martín López Misael 253220165
- Olvera González David 253220060
- Ramos Ángeles Mauro Alberto 253220121

---

# Monitoreo y control — Avance 3

Evaluación intermedia (formativa) — Paso 10 de la metodología CEPAL.

Documento generado con base en el estado real del proyecto al 2026-03-25, contrastando el código fuente, la orquestación de servicios, los registros de Jira y la evidencia técnica funcional del sistema.

---

## Actividad 1 — Análisis de los indicadores de actividades y componentes

| Actividad | Indicador | Meta | Resultado actual | Cumplimiento | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1. Configurar orquestación Docker y pipelines de despliegue | Sistema de contenedores configurado y funcionando | Plataforma operativa en entorno local y desplegable en nube | Orquestación Docker completa (EMQX, MongoDB, backend, frontend, simulador). Pipeline de despliegue automático a EC2 vía GitHub Actions. Infraestructura definida con Terraform. | Alto | Pipeline funcional; despliegue probado en entorno local y remoto. |
| 2. Ensamblar la unidad piloto física y calibrar sensores | Fuente de datos validada, física o emulada | Flujo de adquisición validado con datos equivalentes a lecturas reales | Simulador continuo publicando datos realistas por MQTT. Backend persiste automáticamente cada lectura en MongoDB. Dashboard visualiza datos en tiempo real. | Alto | La validación emulada cubre el ciclo completo sensor→MQTT→BD→Dashboard. La integración física con Raspberry Pi queda como etapa futura. |
| 3. Desarrollar API de clima e integración con modelo Keras | API funcional y módulo predictivo operativo | Sistema capaz de generar predicciones útiles para monitoreo | Backend expone endpoint /api/predict con modelo mock basado en reglas. Frontend tiene cliente REST preparado. Investigación de condiciones óptimas documentada. | Medio | El modelo Keras final sigue pendiente de entrenamiento en Colab. Las reglas mock actuales reflejan umbrales reales validados por la investigación. |
| 4. Implementar Job Cron para generación de datos sintéticos | Automatización continua de generación de datos | Simulación operativa sin depender de sensores reales | Servicio simulator corriendo de forma continua en Docker, publicando en todos los tópicos MQTT del sistema cada 5 segundos. | Alto | Funcional como automatización de datos sintéticos; no implementado como Cron Job explícito sino como servicio permanente, lo cual es equivalente operativamente. |

---

## Actividad 3 — Probabilidad de logro de los objetivos del proyecto

| Nivel del proyecto | Objetivo | Situación actual | Probabilidad de logro | Justificación |
| --- | --- | --- | --- | --- |
| Fin | Contribuir a la soberanía alimentaria urbana mediante tecnología de hidroponía inteligente | Plataforma open source funcional con monitoreo, persistencia, visualización, simulación, autenticación e investigación documentada | Alta | El sistema cuenta con arquitectura replicable, documentación técnica y de investigación, y componentes operativos verificables. |
| Propósito | Implementar una plataforma tecnológica que optimice el cultivo hidropónico | Software principal completado en su base operativa; autenticación, CRUD de usuarios, CRUD de sensores, dashboard con datos REST+MQTT, modelo predictivo mock, e investigación de condiciones óptimas | Alta | El proyecto integra sensores emulados, mensajería MQTT, base de datos, dashboard interactivo, API REST, autenticación y módulo de IA en evolución. |
| Componentes | Sistema de monitoreo, control automatizado y modelo predictivo | Monitoreo en tiempo real, persistencia, alertas, dashboard, login, CRUD completo, modelo relacional documentado e investigación de condiciones óptimas | Media-Alta | Falta integrar el modelo Keras real y validar con hardware físico. Las demás partes están operativas y verificables. |

---

## Actividad 4 — Problemas y acciones

| Problema identificado | Causa | Impacto en el proyecto | Acción correctiva | Responsable |
| --- | --- | --- | --- | --- |
| Disponibilidad de sensores electrónicos | Mercado local limitado y tiempos de adquisición | Retraso en validación con hardware real | Se mantiene simulación como fuente principal de datos; la arquitectura MQTT permite conectar sensores reales sin cambios de código cuando estén disponibles | Equipo de hardware |
| Modelo de IA sigue en modo mock | Falta de datos suficientes para entrenamiento y tiempo de desarrollo del modelo Keras | El endpoint de predicción no genera resultados de IA real | Las reglas mock actuales están basadas en umbrales validados por la investigación; se prepara la integración del modelo exportado desde Colab | Equipo de IA |
| n8n descartado del plan | Complejidad de integración y cambio de estrategia hacia agentes IA | La automatización documental se maneja por otro medio | n8n se reemplazó por agentes IA integrados al flujo de desarrollo (GitHub Copilot agents), cubriendo la automatización documental y operativa | Equipo de desarrollo |
| Conexión frontend-backend parcial en avance 2 | El dashboard consumía solo MQTT y no aprovechaba la API REST | Datos históricos y alertas no visibles al cargar el dashboard | Dashboard actualizado para cargar datos iniciales vía REST al montar, complementando la suscripción MQTT en tiempo real | Equipo de desarrollo |

---

## Tablas independientes por actividad de la fila de actividades

### Actividad 1 — Configuración del sistema (Docker + pipelines)

| Elemento | Descripción |
| --- | --- |
| Indicador | Plataforma Docker funcionando con pipeline de despliegue automático |
| Meta | Sistema desplegado en entorno local y en nube vía CI/CD |
| Medio de verificación | docker-compose.yml operativo, .github/workflows/deploy.yml funcional, infra/main.tf con estado aplicado |
| Supuestos | Disponibilidad de infraestructura AWS y credenciales de despliegue |
| Estado | Cumplida |

### Actividad 2 — Unidad piloto / validación emulada

| Elemento | Descripción |
| --- | --- |
| Indicador | Fuente de datos validada que alimenta todo el ciclo del sistema |
| Meta | Flujo completo: sensor → MQTT → Backend → MongoDB → Dashboard |
| Medio de verificación | Simulador publicando datos cada 5s, lecturas persistidas en MongoDB, visualización en tiempo real en dashboard |
| Supuestos | Broker MQTT operativo; la integración con hardware real depende de disponibilidad de componentes |
| Estado | Cumplida (emulada) |

### Actividad 3 — Integración de IA y API

| Elemento | Descripción |
| --- | --- |
| Indicador | API funcional con módulo predictivo operativo |
| Meta | Endpoint de predicción consumible por el frontend |
| Medio de verificación | POST /api/predict retorna predicción, confianza y recomendaciones; cliente REST del frontend preparado |
| Supuestos | Modelo Keras será entrenado en Colab y exportado; las reglas mock actuales reflejan umbrales validados |
| Estado | Parcial (mock funcional, modelo final pendiente) |

### Actividad 4 — Datos sintéticos

| Elemento | Descripción |
| --- | --- |
| Indicador | Generación automática y continua de datos |
| Meta | Simulación ininterrumpida para pruebas y validación del sistema |
| Medio de verificación | Servicio simulator en Docker, publicaciones MQTT visibles en dashboard y persistidas en MongoDB |
| Supuestos | Broker MQTT disponible y configurado |
| Estado | Cumplida |

### Actividad 5 — Autenticación y gestión de usuarios

| Elemento | Descripción |
| --- | --- |
| Indicador | Sistema de login funcional con CRUD de usuarios |
| Meta | Control de acceso al dashboard y gestión de usuarios del sistema |
| Medio de verificación | POST /api/auth/login, GET/POST/PUT/DELETE /api/users, vista LoginView.vue con guard de autenticación |
| Supuestos | Usuarios de prueba creados automáticamente al iniciar el backend (seed) |
| Estado | Cumplida |

### Actividad 6 — CRUD de sensores y alertas

| Elemento | Descripción |
| --- | --- |
| Indicador | Endpoints REST completos para consulta, historial, estadísticas y gestión de alertas |
| Meta | API que cubra lectura, consulta, estadísticas, eliminación de historial y reconocimiento/eliminación de alertas |
| Medio de verificación | Endpoints: GET /api/sensors/latest, GET /api/sensors/{type}/history, GET /api/sensors/stats, DELETE /api/sensors/{type}/history, GET /api/alerts, PUT /api/alerts/{id}/acknowledge, DELETE /api/alerts/{id} |
| Supuestos | MongoDB operativo con datos persistidos por el suscriptor MQTT |
| Estado | Cumplida |

### Actividad 7 — Modelo relacional

| Elemento | Descripción |
| --- | --- |
| Indicador | Esquema relacional documentado con DDL SQL equivalente |
| Meta | Formalización de la estructura de datos del sistema en formato relacional |
| Medio de verificación | docs/modelo-relacional.md con DDL PostgreSQL, mapeo MongoDB↔SQL y relación con tópicos MQTT |
| Supuestos | El sistema opera con MongoDB; el modelo relacional es documentación de referencia |
| Estado | Cumplida |

### Actividad 8 — Investigación de condiciones óptimas

| Elemento | Descripción |
| --- | --- |
| Indicador | Documento de investigación con rangos óptimos y referencias bibliográficas |
| Meta | Fundamentar los umbrales del sistema con evidencia científica |
| Medio de verificación | docs/investigacion-hidroponia.md con 10 variables documentadas, rangos, impacto y 6 referencias |
| Supuestos | Los umbrales implementados en mqtt_client.py coinciden con la literatura |
| Estado | Cumplida |

### Actividad descartada — n8n

| Elemento | Descripción |
| --- | --- |
| Indicador | N/A |
| Meta | Lanzamiento de n8n para automatización con agentes |
| Medio de verificación | N/A |
| Supuestos | N/A |
| Estado | Descartada — se reemplazó por agentes IA integrados al flujo de desarrollo (GitHub Copilot agents) |

---

## Resumen actualizado de actividades (Jira KAN al 2026-03-25)

| Resumen | Estado | Persona asignada | Parent summary |
| --- | --- | --- | --- |
| Organización | Finalizado | David Olvera González | Organización |
| Cotización | Finalizado | Mauro Alberto Ramos Ángeles | Organización |
| Diseño | Finalizado | David Olvera González | Organización |
| Infraestructura y sistema Base | Finalizado | Mauro Alberto Ramos Ángeles | Infraestructura |
| Crear instancia AWS | Finalizado | Misael Martín López | Infraestructura |
| Configurar plataforma base | Finalizado | José Andrés Bardales Calva | Infraestructura |
| Lanzamiento frontend | Finalizado | Misael Martín López | Infraestructura |
| Lanzamiento backend FastAPI | Finalizado | David Olvera González | Infraestructura |
| Lanzamiento MongoDB | Finalizado | David Olvera González | Infraestructura |
| Lanzamiento EMQX | Finalizado | David Olvera González | Infraestructura |
| Lanzamiento n8n | Descartada | Mauro Alberto Ramos Ángeles | Infraestructura |
| Configurar servidor MQTT | Finalizado | Mauro Alberto Ramos Ángeles | Backend |
| Función MQTT → registrar sensores en BD | Finalizado | Misael Martín López | Backend |
| Función MQTT → alarmas y alertas | Finalizado | Misael Martín López | Backend |
| CRUD historial de lectura de sensores | Finalizado | José Andrés Bardales Calva | Backend |
| CRUD usuarios y login | Finalizado | José Andrés Bardales Calva | Backend |
| Pipeline despliegue backend | Finalizado | José Andrés Bardales Calva | Backend |
| Crear diseño inicial | Finalizado | David Olvera González | Frontend Dashboard |
| Construir esqueleto Vue.js | Finalizado | Mauro Alberto Ramos Ángeles | Frontend Dashboard |
| Construir login | Finalizado | Mauro Alberto Ramos Ángeles | Frontend Dashboard |
| Conectar con MQTT (EMQX) | Finalizado | David Olvera González | Frontend Dashboard |
| Conectar frontend con endpoints backend | Finalizado | David Olvera González | Frontend Dashboard |
| Pipeline despliegue frontend | Finalizado | Mauro Alberto Ramos Ángeles | Frontend Dashboard |
| Configurar persistencia MongoDB | Finalizado | David Olvera González | Base Datos |
| Modelo relacional | Finalizado | David Olvera González | Base Datos |
| Servicio datos sintéticos | Finalizado | Mauro Alberto Ramos Ángeles | Datos sintéticos |
| Investigación condiciones óptimas | Finalizado | José Andrés Bardales Calva | Investigación |

---

## Observaciones finales

1. Todas las actividades reportadas como "Cumplida" tienen evidencia técnica verificable en el repositorio del proyecto.
2. La actividad de n8n fue descartada formalmente y reemplazada por agentes IA integrados al flujo de desarrollo.
3. El modelo relacional se documentó como esquema SQL equivalente sin migrar la base de datos, ya que MongoDB sigue siendo la mejor opción técnica para el proyecto.
4. La investigación de condiciones óptimas en hidroponía fundamenta los umbrales implementados en el sistema de alertas.
5. El modelo de IA sigue en modo mock con reglas basadas en umbrales validados; el modelo Keras final será integrado cuando se complete el entrenamiento en Colab.
6. La validación con hardware real queda como etapa posterior; la validación emulada cubre todo el flujo del sistema.
