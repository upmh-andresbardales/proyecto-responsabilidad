# Propuesta de segunda entrega para el equipo

Proyecto: Sistema de Monitoreo Acuapónico Inteligente

Fecha de corte: 2026-03-18

## 1. Qué pide la tarea

La consigna de `Monitoreo y control, 2` indica que, con base en la metodología de marco lógico de la CEPAL, debemos entregar las tablas correspondientes a:

1. Actividad 1. Análisis de los indicadores de actividades y componentes.
2. Actividad 3. Probabilidad de logro de los objetivos del proyecto.
3. Actividad 4. Problemas y acciones.

Además, la fila de actividades de la matriz del marco lógico debe presentarse en tablas independientes para facilitar la revisión.

## 2. Cómo se propone abordar la segunda entrega

La propuesta no es cambiar radicalmente la primera entrega, sino actualizarla como avance intermedio con base en lo que sí tenemos implementado hoy.

El criterio propuesto para reportar estado es:

- `Cerrado`: ya implementado y verificable en el proyecto.
- `En progreso`: ya existe una base funcional, pero aún falta cierre o integración final.
- `Por hacer`: aún no hay validación suficiente o depende de etapas posteriores.

## 3. Qué se conserva de la primera entrega del PDF

De la primera entrega se conserva la estructura general:

- actividades del proyecto
- indicadores
- metas
- resultado actual
- cumplimiento
- observaciones
- probabilidad de logro del proyecto
- tabla de problemas y acciones
- tablas independientes por actividad

Lo que cambia es la redacción de algunas actividades para que se apeguen al estado real del repositorio y no prometan más de lo que hoy se puede demostrar.

## 4. Actividades base del PDF y ajuste propuesto

| Actividad de la primera entrega | Lectura actual del equipo | Ajuste propuesto para segunda entrega |
| --- | --- | --- |
| Configurar orquestación Docker y pipelines de despliegue | Ya existe base funcional local y en AWS | Reportarla como plataforma base de despliegue local y en nube |
| Ensamblar unidad piloto física y calibrar sensores | La parte física completa aún no está cerrada | Reformularla como validación emulada de adquisición de datos con Raspberry Pi y datasets reales |
| Desarrollar API de clima e integración con modelo Keras | Ya existe backend y endpoint de predicción, pero el modelo real aún no está integrado | Reportarla como integración de API y módulo predictivo en progreso |
| Implementar Job Cron para generación de datos sintéticos | Ya existe simulador continuo, aunque no scheduler formal | Reportarla como servicio automatizado de generación de datos sintéticos |

## 5. Propuesta final de actividades para reportar

### Actividades cerradas

1. Configurar la plataforma base de despliegue local y en nube.
2. Integrar la comunicación en tiempo real mediante MQTT.
3. Implementar persistencia y gestión de alertas del sistema.
4. Desarrollar dashboard de monitoreo en tiempo real.

### Actividades en progreso

1. Implementar servicio automatizado de generación de datos sintéticos.
2. Desarrollar API de consulta histórica y analítica básica.
3. Integrar módulo predictivo para apoyo a decisiones.
4. Validar integración emulada de adquisición de datos con apoyo de Raspberry Pi y datasets reales.

### Actividades por hacer

1. Integración física final con sensores reales.
2. Calibración final de sensores en entorno piloto.
3. Integración de modelo predictivo definitivo entrenado con datos validados.

## 6. Propuesta de tablas para entregar

## Actividad 1. Análisis de los indicadores de actividades y componentes

| Actividad | Estado actual | Indicador | Meta | Resultado actual | Cumplimiento | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Configurar la plataforma base de despliegue local y en nube | Cerrado | Plataforma con contenedores, infraestructura y despliegue operativo | Sistema desplegado en entorno local y preparado para despliegue remoto | Docker Compose funcional, infraestructura en AWS definida con Terraform y despliegue automatizado básico a EC2 | Alto | La plataforma base ya opera a nivel de software e infraestructura |
| 2. Integrar la comunicación en tiempo real mediante MQTT | Cerrado | Broker y clientes conectados para intercambio de telemetría | Flujo de datos en tiempo real entre simulador, backend y dashboard | EMQX configurado; backend suscrito a tópicos; frontend conectado vía WebSocket; tópicos definidos y documentados | Alto | La integración básica y la definición de tópicos ya pueden considerarse cerradas |
| 3. Implementar persistencia y gestión de alertas del sistema | Cerrado | Registro de lecturas y alertas en base de datos | Sistema capaz de almacenar telemetría y generar alertas automáticas | MongoDB integrado; lecturas persistidas desde MQTT; alertas generadas por umbrales | Alto | El backend ya resuelve persistencia y alertamiento |
| 4. Desarrollar dashboard de monitoreo en tiempo real | Cerrado | Interfaz web funcional para visualización del sistema | Dashboard con indicadores, series temporales y alertas visibles | Dashboard en Vue con gauges, gráficas, estado del sistema y panel de alertas | Alto | La visualización principal ya está operativa |
| 5. Implementar servicio automatizado de generación de datos sintéticos | En progreso | Simulación continua de datos para pruebas | Disponibilidad de datos de prueba sin depender de sensores físicos | Simulador Python funcional con publicación MQTT de múltiples sensores y escenarios | Medio-Alto | El flujo existe; puede fortalecerse con scheduler explícito o mayor control operativo |
| 6. Desarrollar API de consulta histórica y analítica básica | En progreso | Endpoints para histórico, estadísticas y alertas | Sistema capaz de consultar histórico y métricas por sensor | API REST con consultas de últimas lecturas, historial, estadísticas y alertas | Medio | La API ya existe, pero todavía puede explotarse mejor desde el frontend |
| 7. Integrar módulo predictivo para apoyo a decisiones | En progreso | Servicio de predicción disponible para el sistema | Generación de predicciones sobre el estado del cultivo | Endpoint de predicción implementado con lógica mock y estructura lista para modelo real | Medio | El siguiente paso es integrar un modelo entrenado y validado |
| 8. Validar integración emulada de adquisición de datos con apoyo de Raspberry Pi y datasets reales | En progreso | Flujo de datos emulado desde un dispositivo intermedio con datos realistas | Sistema capaz de recibir datos equivalentes a una fuente física sin depender de sensores finales | Actualmente se plantea usar Raspberry Pi para emular la conexión de sensores con datasets reales o históricos adaptados al formato MQTT | Medio | Esta estrategia permite validar integración sin bloquearse por la ausencia de hardware final |

## Actividad 3. Probabilidad de logro de los objetivos del proyecto

| Nivel del proyecto | Objetivo | Situación actual | Probabilidad de logro | Justificación |
| --- | --- | --- | --- | --- |
| Fin | Contribuir al monitoreo y optimización de sistemas de cultivo acuapónico mediante una plataforma tecnológica accesible | El proyecto ya cuenta con una base funcional de monitoreo, simulación, persistencia, visualización y despliegue | Alta | La arquitectura principal está implementada y puede seguir madurando de manera incremental |
| Propósito | Implementar una plataforma tecnológica para monitoreo en tiempo real, registro de datos y apoyo a decisiones | Existe integración entre simulador, broker MQTT, backend, base de datos, dashboard web y despliegue remoto | Alta | El núcleo funcional ya opera; lo pendiente corresponde a consolidación y validación avanzada |
| Componentes | Monitoreo en tiempo real, persistencia, alertas, visualización, analítica básica y predicción | Los componentes principales del software están implementados; la siguiente validación se propone mediante Raspberry Pi y datasets reales | Alta | La falta de hardware final no bloquea el avance, porque puede validarse la capa de adquisición mediante emulación realista |

## Actividad 4. Problemas y acciones

| Problema identificado | Causa | Impacto en el proyecto | Acción correctiva | Responsable |
| --- | --- | --- | --- | --- |
| Falta de integración física final con sensores reales | Disponibilidad limitada de sensores y necesidad de calibración | Retraso en la validación física completa del sistema piloto | Sustituir temporalmente la validación física por una emulación con Raspberry Pi y datasets reales o históricos | Equipo de hardware |
| Módulo predictivo aún no conectado a modelo real | Falta de datos suficientes y proceso de entrenamiento pendiente | La predicción actual funciona como prototipo lógico | Integrar modelo exportado y validar salidas con datos históricos o simulados | Equipo de IA |
| Uso parcial de la API REST en el frontend | El dashboard actual prioriza consumo MQTT en tiempo real | La analítica histórica aún no se explota al máximo en la interfaz | Conectar vistas del frontend con endpoints de histórico, estadísticas y alertas | Equipo de frontend |
| Automatización de datos sintéticos no formalizada como scheduler | El simulador actual corre como servicio continuo | Puede existir diferencia entre lo implementado y la redacción original del plan | Ajustar redacción del entregable o agregar scheduler explícito si se considera necesario | Equipo de desarrollo |
| Falta de autenticación de usuarios | El enfoque inicial se centró en el núcleo de monitoreo | La plataforma aún no cuenta con control de acceso formal | Dejar autenticación como siguiente fase funcional posterior al cierre del monitoreo base | Equipo backend |

## 7. Tablas independientes de actividades

### Actividad 1. Plataforma base de despliegue

| Elemento | Descripción |
| --- | --- |
| Estado actual | Cerrado |
| Indicador | Plataforma desplegable en entorno local y nube |
| Meta | Sistema base operativo con contenedores, despliegue remoto e infraestructura documentada |
| Medio de verificación | Docker Compose funcional, despliegue remoto y archivos Terraform |
| Supuestos | Disponibilidad de infraestructura y credenciales de despliegue |

### Actividad 2. Monitoreo y persistencia de datos

| Elemento | Descripción |
| --- | --- |
| Estado actual | Cerrado |
| Indicador | Flujo funcional de datos desde fuente emisora hacia backend, base de datos y dashboard |
| Meta | Sistema capaz de recibir, almacenar y visualizar telemetría en tiempo real |
| Medio de verificación | Tópicos MQTT activos, registros en MongoDB, alertas generadas y dashboard operativo |
| Supuestos | Disponibilidad del broker MQTT, base de datos y conectividad entre servicios |

### Actividad 3. Integración de API y módulo predictivo

| Elemento | Descripción |
| --- | --- |
| Estado actual | En progreso |
| Indicador | API funcional con servicios de consulta y predicción |
| Meta | Sistema capaz de ofrecer histórico, estadísticas y apoyo predictivo al monitoreo |
| Medio de verificación | Respuestas de endpoints REST y ejecución del servicio de predicción |
| Supuestos | Disponibilidad de datos consistentes e integración posterior del modelo definitivo |

### Actividad 4. Generación de datos sintéticos para pruebas

| Elemento | Descripción |
| --- | --- |
| Estado actual | En progreso |
| Indicador | Servicio de simulación automática de datos de sensores |
| Meta | Mantener un flujo continuo de datos de prueba para validar el sistema sin hardware físico |
| Medio de verificación | Publicación periódica en MQTT y consumo por backend y frontend |
| Supuestos | Correcta ejecución del simulador y estabilidad del broker MQTT |

### Actividad 5. Validación emulada de adquisición de datos

| Elemento | Descripción |
| --- | --- |
| Estado actual | En progreso |
| Indicador | Emulación funcional de una fuente de datos equivalente a sensores mediante Raspberry Pi y datasets reales |
| Meta | Validar el flujo de adquisición, publicación y consumo sin depender de sensores físicos definitivos |
| Medio de verificación | Publicación de lecturas desde Raspberry Pi o servicio equivalente, persistencia en backend y visualización en dashboard |
| Supuestos | Disponibilidad de Raspberry Pi, acceso a datasets reales y adaptación del formato de datos al esquema del proyecto |

## 8. Alcance propuesto de mejora para esta segunda entrega

La propuesta de mejora para esta segunda entrega es reportar como cerradas las partes del sistema que ya están funcionales y verificables, y como en progreso aquellas que sí pueden avanzar en esta etapa con apoyo de agentes IA y trabajo incremental del equipo.

### Alcance que sí podemos comprometernos a lograr

1. Mantener cerrada la integración básica MQTT y la definición de tópicos.
2. Consolidar el flujo de datos sintéticos y documentar mejor su operación.
3. Conectar el frontend con más endpoints REST para histórico y analítica básica.
4. Mejorar el módulo predictivo actual mediante reglas de apoyo a decisiones mientras se integra el modelo final.
5. Implementar una validación emulada de adquisición de datos usando Raspberry Pi y datasets reales o históricos.

### Alcance que conviene dejar fuera de esta etapa

1. Integración física final con todos los sensores reales.
2. Calibración final de sensores en entorno piloto.
3. Cierre total del modelo predictivo definitivo entrenado con datos propios validados.

## 9. Conclusión para compartir con el equipo

La segunda entrega debe presentarse como un avance intermedio realista. Ya podemos reportar como cerrados los componentes centrales del sistema: plataforma base, integración MQTT, definición de tópicos, persistencia, alertas y dashboard. En cambio, la explotación analítica, el fortalecimiento del módulo predictivo y la validación emulada con Raspberry Pi y datasets reales deben reportarse como actividades en progreso. La parte física final puede mantenerse como fase posterior sin debilitar la entrega, siempre que se explique que la validación de adquisición se realizará de forma emulada y verificable.