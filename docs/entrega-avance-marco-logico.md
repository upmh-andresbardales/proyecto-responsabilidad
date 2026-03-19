# Monitoreo y control 2 - Avance del proyecto

Proyecto: Sistema de Monitoreo Acuapónico Inteligente

Fecha de corte: 2026-03-18

## Actividad 1. Análisis de los indicadores de actividades y componentes

| Actividad | Estado actual | Indicador | Meta | Resultado actual | Cumplimiento | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Configurar la plataforma base de despliegue local y en nube | Cerrado | Plataforma con contenedores, infraestructura y despliegue operativo | Sistema desplegado en entorno local y preparado para despliegue remoto | Docker Compose funcional, infraestructura en AWS definida con Terraform y despliegue automatizado básico a EC2 | Alto | La plataforma base ya opera a nivel de software e infraestructura; faltan pruebas más formales por componente |
| 2. Integrar la comunicación en tiempo real mediante MQTT | Cerrado | Broker y clientes conectados para intercambio de telemetría | Flujo de datos en tiempo real entre simulador, backend y dashboard | EMQX configurado; backend suscrito a tópicos de sensores; frontend conectado vía WebSocket; tópicos definidos y documentados | Alto | La integración MQTT ya está funcional y permite monitoreo en tiempo real |
| 3. Implementar persistencia y gestión de alertas del sistema | Cerrado | Registro de lecturas y alertas en base de datos | Sistema capaz de almacenar telemetría y generar alertas automáticas | MongoDB integrado; lecturas persistidas desde MQTT; alertas generadas por umbrales y publicadas al sistema | Alto | El componente backend ya cubre persistencia y alertamiento automático |
| 4. Desarrollar dashboard de monitoreo en tiempo real | Cerrado | Interfaz web funcional para visualización del sistema | Dashboard con indicadores, series temporales y alertas visibles | Dashboard en Vue con gauges, gráficos temporales, estado del sistema y panel de alertas | Alto | La visualización principal está implementada y conectada al flujo MQTT |
| 5. Implementar servicio automatizado de generación de datos sintéticos | En progreso | Simulación continua de datos para pruebas | Disponibilidad de datos de prueba sin depender de sensores físicos | Simulador Python funcional con publicación MQTT de 10 sensores y escenarios de prueba | Medio-Alto | Ya existe simulación continua; queda pendiente formalizarlo como scheduler si se requiere estrictamente un Cron Job |
| 6. Desarrollar API de consulta histórica y analítica básica | En progreso | Endpoints para histórico, estadísticas y alertas | Sistema capaz de consultar histórico y métricas por sensor | API REST con consultas de últimas lecturas, historial, estadísticas y alertas | Medio | La API ya existe, pero su aprovechamiento completo desde frontend aún puede mejorar |
| 7. Integrar módulo predictivo para apoyo a decisiones | En progreso | Servicio de predicción disponible para el sistema | Generación de predicciones sobre el estado del cultivo | Endpoint de predicción implementado con lógica mock y estructura lista para modelo real | Medio | Falta integrar el modelo Keras definitivo y validar con datos reales |
| 8. Validar integración emulada de adquisición de datos con apoyo de Raspberry Pi y datasets reales | En progreso | Flujo de datos emulado desde un dispositivo intermedio con datos realistas | Sistema capaz de recibir datos con estructura equivalente a una fuente física, aun sin sensores finales conectados | Actualmente se cuenta con simulación sintética funcional y se plantea usar Raspberry Pi para emular la conexión de sensores a partir de datasets reales | Medio | Esta ruta permite validar integración y comportamiento del sistema sin depender de la disponibilidad inmediata del hardware final |

## Actividad 3. Probabilidad de logro de los objetivos del proyecto

| Nivel del proyecto | Objetivo | Situación actual | Probabilidad de logro | Justificación |
| --- | --- | --- | --- | --- |
| Fin | Contribuir al monitoreo y optimización de sistemas de cultivo acuapónico mediante una plataforma tecnológica accesible | El proyecto ya cuenta con plataforma digital funcional de monitoreo, simulación y despliegue | Alta | La solución base ya está desarrollada y puede evolucionar sobre una arquitectura reutilizable |
| Propósito | Implementar una plataforma tecnológica para monitoreo en tiempo real, registro de datos y apoyo a decisiones | Existe integración entre simulador, broker MQTT, backend, base de datos, dashboard web y despliegue en nube | Alta | El núcleo del sistema ya opera; las brechas restantes son de madurez funcional, no de viabilidad técnica |
| Componentes | Monitoreo en tiempo real, persistencia, alertas, visualización, analítica básica y predicción | Los componentes principales del software están implementados; la siguiente validación se plantea mediante emulación con Raspberry Pi y datasets reales, mientras el modelo predictivo final sigue pendiente | Alta | La mayor parte del sistema ya está construida y la validación emulada permite avanzar sin bloquearse por la falta de sensores físicos definitivos |

## Actividad 4. Problemas y acciones

| Problema identificado | Causa | Impacto en el proyecto | Acción correctiva | Responsable |
| --- | --- | --- | --- | --- |
| Falta de integración con hardware real final | Disponibilidad limitada de sensores y necesidad de calibración | Retraso en la validación física completa del sistema piloto | Sustituir temporalmente la validación física final por una emulación de adquisición usando Raspberry Pi y datasets reales o históricos | Equipo de hardware |
| Módulo predictivo aún no conectado a modelo real | Falta de datos suficientes y proceso de entrenamiento pendiente | La predicción actual funciona solo como prototipo lógico | Integrar modelo Keras entrenado y validar resultados con datos históricos o simulados | Equipo de IA |
| Uso parcial de la API REST en el frontend | El dashboard actual prioriza consumo por MQTT en tiempo real | El componente histórico y analítico no está explotado al máximo en la interfaz | Conectar vistas del frontend con endpoints de histórico, estadísticas y alertas | Equipo de frontend |
| Ausencia de autenticación de usuarios | El enfoque inicial se concentró en el núcleo de monitoreo | La plataforma aún no cuenta con control de acceso formal | Diseñar e implementar módulo de usuarios y login como siguiente fase funcional | Equipo backend |
| Automatización de datos sintéticos no formalizada como scheduler | El simulador actual se ejecuta como servicio continuo | Puede observarse diferencia entre lo implementado y la redacción original del plan | Ajustar la redacción del entregable o incorporar scheduler explícito si el requisito académico lo exige | Equipo de desarrollo |

## Tablas independientes de actividades de la matriz del marco lógico

### Actividad 1. Plataforma base de despliegue

| Elemento | Descripción |
| --- | --- |
| Estado actual | Cerrado |
| Indicador | Plataforma desplegable en entorno local y nube |
| Meta | Sistema base operativo con contenedores, despliegue remoto e infraestructura documentada |
| Medio de verificación | Ejecución mediante Docker Compose, workflow de despliegue y archivos Terraform |
| Supuestos | Disponibilidad de infraestructura, acceso a servicios cloud y credenciales de despliegue |

### Actividad 2. Monitoreo y persistencia de datos

| Elemento | Descripción |
| --- | --- |
| Estado actual | Cerrado |
| Indicador | Flujo funcional de datos desde sensores simulados hacia backend, base de datos y dashboard |
| Meta | Sistema capaz de recibir, almacenar, consultar y visualizar telemetría en tiempo real |
| Medio de verificación | Tópicos MQTT activos, registros en MongoDB, endpoints REST y dashboard operativo |
| Supuestos | Disponibilidad del broker MQTT, base de datos y conectividad entre servicios |

### Actividad 3. Integración de API y módulo predictivo

| Elemento | Descripción |
| --- | --- |
| Estado actual | En progreso |
| Indicador | API funcional con servicios de consulta y predicción |
| Meta | Sistema capaz de ofrecer histórico, estadísticas y predicciones de apoyo al monitoreo |
| Medio de verificación | Respuestas de endpoints REST y ejecución del servicio de predicción |
| Supuestos | Disponibilidad de datos consistentes y posterior integración del modelo predictivo final |

### Actividad 4. Generación de datos sintéticos para pruebas

| Elemento | Descripción |
| --- | --- |
| Estado actual | En progreso |
| Indicador | Servicio de simulación automática de datos de sensores |
| Meta | Mantener un flujo continuo de datos de prueba para validar el sistema sin hardware físico |
| Medio de verificación | Publicación periódica de datos en MQTT y visualización en backend y frontend |
| Supuestos | Correcta ejecución del simulador, disponibilidad del broker MQTT y estabilidad de la orquestación |

### Actividad 5. Validación emulada de adquisición de datos

| Elemento | Descripción |
| --- | --- |
| Estado actual | En progreso |
| Indicador | Emulación funcional de una fuente de datos equivalente a sensores usando Raspberry Pi y datasets reales |
| Meta | Validar el flujo de adquisición, publicación y consumo de datos sin depender de sensores físicos definitivos |
| Medio de verificación | Publicación de lecturas desde Raspberry Pi o servicio equivalente, consumo por MQTT, persistencia en backend y visualización en dashboard |
| Supuestos | Disponibilidad de Raspberry Pi, acceso a datasets reales o históricos y adaptación del formato de datos al esquema del proyecto |

## Alcance propuesto para la siguiente etapa con apoyo de agentes IA

| Línea de trabajo | Estado actual | Alcance propuesto | Viabilidad |
| --- | --- | --- | --- |
| Integración básica MQTT y definición de tópicos | Cerrado | Mantener estable y documentado el flujo actual sin cambiar la arquitectura base | Alta |
| Consumo REST en frontend para histórico y métricas | En progreso | Conectar el dashboard a endpoints existentes de histórico, estadísticas y alertas | Alta |
| Reglas de apoyo a decisiones | En progreso | Mejorar el módulo predictivo mock con reglas más completas y recomendaciones automáticas asistidas por IA | Alta |
| Automatización documental y operativa | En progreso | Usar agentes IA para mantener documentación técnica, tablas de seguimiento y validaciones de consistencia | Alta |
| Integración de modelo IA entrenado | En progreso | Preparar contrato de entrada y salida del modelo y dejar listo el backend para integrar un modelo exportado | Media |
| Emulación de sensores con Raspberry Pi y datasets reales | En progreso | Implementar un emulador que publique lecturas realistas desde un dataset adaptado al esquema MQTT del proyecto | Alta |
| Hardware real y calibración final | Por hacer | Mantener fuera del alcance inmediato hasta contar con sensores y pruebas físicas definitivas | Baja |

### Cierre sugerido del avance

Con base en la evaluación intermedia, se considera que la fase de infraestructura base, integración MQTT, definición de tópicos, persistencia de datos, alertamiento y visualización en tiempo real puede reportarse como cerrada. Las actividades relacionadas con explotación analítica, fortalecimiento del módulo predictivo y automatización complementaria se mantienen en progreso. En sustitución de la validación física completa, se propone como siguiente alcance una validación emulada de adquisición de datos con Raspberry Pi y datasets reales, dejando la integración final con sensores físicos como actividad posterior.

## Nota de interpretación del avance

La entrega corresponde a un avance intermedio del proyecto. Por ello, las tablas distinguen entre componentes ya implementados, componentes en progreso y elementos aún pendientes de validación final. En particular, la parte física puede reportarse en esta etapa como validación emulada con Raspberry Pi y datasets reales, mientras la integración definitiva con sensores y calibración queda para una fase posterior.