# Universidad Politecnica Metropolitana de Hidalgo

## Carrera: Maestria en Inteligencia Artificial

### CUATRIMESTRE 2

- Grupo: Unico
- Nombre del Equipo: OptiMind Four
- Docente: Dr. Victor Dario Cuervo Pinto
- Materia: Responsabilidad Social

### Integrantes

- Bardales Calva Jose Andres - 253220002
- Martin Lopez Misael - 253220165
- Olvera Gonzalez David - 253220060
- Ramos Angeles Mauro Alberto - 253220121

# Monitoreo y control

Documento actualizado con base en el avance real del proyecto al 2026-03-18.

## Actividad 1 - Analisis de los indicadores de actividades y componentes

| Actividad | Indicador | Meta | Resultado actual | Cumplimiento | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1. Configurar orquestacion Docker y pipelines de despliegue | Sistema de contenedores configurado y funcionando | Plataforma operativa en entorno local y preparada para despliegue remoto | Orquestacion Docker funcional, despliegue remoto automatizado basico en EC2 y base de infraestructura en AWS definida con Terraform | Alto | Permite desplegar la plataforma del sistema; falta fortalecer validaciones formales del pipeline |
| 2. Ensamblar la unidad piloto fisica y calibrar sensores | Nodo sensor funcional o equivalente de adquisicion validado | Unidad piloto de hidroponia o flujo de adquisicion validado | La validacion fisica completa sigue pendiente; se propone validacion emulada con Raspberry Pi y datasets reales o historicos para simular la adquisicion | Medio | Reduce dependencia del hardware final y permite validar la arquitectura con datos realistas |
| 3. Desarrollar API de clima e integracion con modelo Keras | API conectada con el sistema y modulo predictivo disponible | Integracion de servicios de datos y prediccion del sistema | Backend funcional con endpoints de consulta y prediccion; el modelo predictivo actual sigue en modo mock y falta integrar el modelo final | Medio | Requiere pruebas con datos reales o historicos y conexion del modelo definitivo |
| 4. Implementar Job Cron para generacion de datos sinteticos | Automatizacion de generacion de datos | Sistema capaz de simular datos para pruebas | Existe simulador continuo publicando datos por MQTT; no se ha formalizado aun como Cron Job explicito | Alto | Permite pruebas sin depender de sensores reales; puede reportarse como automatizacion funcional de datos sinteticos |

## Actividad 3 - Probabilidad de logro de los objetivos del proyecto

| Nivel del proyecto | Objetivo | Situacion actual | Probabilidad de logro | Justificacion |
| --- | --- | --- | --- | --- |
| Fin | Contribuir a la soberania alimentaria urbana mediante tecnologia de hidroponia inteligente | Desarrollo de plataforma open source funcional de monitoreo, persistencia, visualizacion y simulacion | Alta | El sistema ya cuenta con una arquitectura replicable y componentes base operativos |
| Proposito | Implementar una plataforma tecnologica que optimice el cultivo hidroponico | Desarrollo del software principal completado en su base; validacion de adquisicion y consolidacion predictiva en progreso | Alta | El proyecto combina sensores o emulacion de sensores, software, mensajeria MQTT, base de datos, dashboard e IA en evolucion |
| Componentes | Sistema de monitoreo, control automatizado y modelo predictivo | Monitoreo en tiempo real, persistencia, alertas y dashboard ya implementados; validacion emulada con Raspberry Pi y modelo predictivo final en progreso | Media-Alta | Algunas partes siguen dependiendo de validacion avanzada, integracion de modelo real y pruebas de adquisicion emulada o fisica |

## Actividad 4 - Problemas y acciones

| Problema identificado | Causa | Impacto en el proyecto | Accion correctiva | Responsable |
| --- | --- | --- | --- | --- |
| Disponibilidad de sensores electronicos | Mercado local limitado y tiempos de adquisicion | Retraso en pruebas del sistema fisico | Sustituir temporalmente las pruebas fisicas por simulacion de datos y emulacion de adquisicion con Raspberry Pi y datasets reales | Equipo de hardware |
| Integracion entre software y hardware | Diferencias en protocolos, comunicacion y disponibilidad del nodo fisico final | Posible retraso en pruebas integrales del sistema | Implementar pruebas con datos sinteticos y una etapa de emulacion controlada de adquisicion antes del hardware final | Equipo de desarrollo |
| Validacion del modelo de IA | Necesidad de suficientes datos y falta de modelo final integrado | Limitacion en entrenamiento y validacion del modelo | Generar datos simulados, aprovechar datasets historicos o externos y preparar la integracion del modelo exportado | Equipo de IA |

## Actividad 1 - Configuracion del sistema

| Elemento | Descripcion |
| --- | --- |
| Indicador | Plataforma Docker funcionando |
| Meta | Sistema desplegado en entorno local y preparado para despliegue remoto |
| Medio de verificacion | Pruebas de ejecucion del sistema, Docker Compose, workflow de despliegue y configuracion de infraestructura |
| Supuestos | Disponibilidad de infraestructura, software y credenciales de despliegue |

## Actividad 2 - Unidad piloto

| Elemento | Descripcion |
| --- | --- |
| Indicador | Fuente de datos validada, ya sea fisica o emulada |
| Meta | Validar el flujo de adquisicion para el sistema piloto mediante sensores reales o emulacion con Raspberry Pi |
| Medio de verificacion | Lecturas publicadas por MQTT, persistidas en backend y visibles en el dashboard |
| Supuestos | Disponibilidad de componentes electronicos o de Raspberry Pi y datasets reales adaptables |

## Actividad 3 - Integracion de IA y API

| Elemento | Descripcion |
| --- | --- |
| Indicador | API funcional y modulo predictivo integrado a nivel operativo |
| Meta | Sistema capaz de generar predicciones y consultas utiles para monitoreo |
| Medio de verificacion | Resultados de endpoints de consulta y salida del servicio de prediccion |
| Supuestos | Disponibilidad de datos suficientes y posterior integracion del modelo final |

## Actividad 4 - Datos sinteticos

| Elemento | Descripcion |
| --- | --- |
| Indicador | Generacion automatica de datos |
| Meta | Simulacion continua de datos para pruebas |
| Medio de verificacion | Registros del sistema, publicaciones MQTT y visualizacion en frontend |
| Supuestos | Correcta operacion del simulador o de la programacion del servicio automatizado |

## Resumen actualizado de actividades

Las actividades de esta tabla corresponden al estado actual registrado en Jira del proyecto `KAN`, ya ajustado para reflejar el avance real del proyecto.

| Resumen | Estado actual | Tipo de proyecto | Persona asignada | Prioridad | Creada | Actualizada | Fecha de vencimiento | Parent summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Funcion subscrita a topicos mqtt para alarmas y alertas | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:23 | 18/03/2026 23:41 | 10/04/2026 | Backend |
| Funcion suscrita a topicos mqtt para registrar sensores en BD | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:22 | 18/03/2026 23:41 | 11/04/2026 | Backend |
| CRUD historial de lectura de sensores | En curso | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:22 | 18/03/2026 23:41 | 11/04/2026 | Backend |
| CRUD usuarios y login | Por hacer | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:21 | 18/03/2026 23:41 | 03/04/2026 | Backend |
| Configurar y probar pipeline de despliege (backend) | En curso | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:21 | 18/03/2026 23:42 | 07/04/2026 | Backend |
| Modelo relacional | Por hacer | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:21 | 12/03/2026 00:22 | 02/04/2026 | Base Datos |
| Configurar y probar pipeline de despliege FRONT | En curso | software | MAURO ALBERTO RAMOS ANGELES | Medium | 27/02/2026 00:20 | 18/03/2026 23:42 | 02/04/2026 | Frontend Dashboard |
| Lanzamiento n8n para trabajar con agentes | Por hacer | software | MAURO ALBERTO RAMOS ANGELES | Medium | 27/02/2026 00:20 | 12/03/2026 00:19 | 04/04/2026 | Infraestructura y sistema Base |
| Lanzamiento EMQX | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:42 | 04/04/2026 | Infraestructura y sistema Base |
| Lanzamiento Mongo DB | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:42 | 03/04/2026 | Infraestructura y sistema Base |
| Lanzamiento de backend fast api | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:42 | 03/04/2026 | Infraestructura y sistema Base |
| Lanzamiento de frontend | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:41 | 26/03/2026 | Infraestructura y sistema Base |
| Configrar plataforma base para lanzamiento de aplicaciones | Finalizado | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:19 | 18/03/2026 23:09 | 01/04/2026 | Infraestructura y sistema Base |
| Crear instancia AWS | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:18 | 18/03/2026 23:09 | 19/03/2026 | Infraestructura y sistema Base |
| Base Datos | En curso | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:31 | 18/03/2026 23:41 | Sin fecha | Base Datos |
| Investigacion condiciones optimas en hidroponia | Por hacer | software | JOSE ANDRES BARDALES CALVA | Medium | 24/02/2026 21:26 | 12/03/2026 00:22 | 08/04/2026 | Investigacion |
| generar servicio para datos sinteticos (n8n o fastapi) | En curso | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:24 | 18/03/2026 23:41 | 04/04/2026 | Datos sinteticos |
| Configurar Servidor MQTT | Finalizado | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:23 | 18/03/2026 23:01 | Sin fecha | Backend |
| Conectar con mqtt(emqx) | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:24 | 18/03/2026 23:41 | 01/04/2026 | Frontend Dashboard |
| Conectar frontend con endpoints de backend | En curso | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:24 | 18/03/2026 23:09 | 20/03/2026 | Frontend Dashboard |
| Backend | En curso | software | MISAEL MARTIN LOPEZ | Medium | 24/02/2026 21:23 | 18/03/2026 22:54 | 11/04/2026 | Backend |
| Construir login | Por hacer | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:23 | 18/03/2026 23:41 | 13/03/2026 | Frontend Dashboard |
| Construir el esquelo en vuejs | Finalizado | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:23 | 18/03/2026 23:41 | 08/03/2026 | Frontend Dashboard |
| Crear diseno inicial o bosquejo | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:22 | 18/03/2026 23:41 | 04/03/2026 | Frontend Dashboard |
| Frontend Dashboard | En curso | software | JOSE ANDRES BARDALES CALVA | Medium | 24/02/2026 21:22 | 18/03/2026 22:54 | 03/04/2026 | Frontend Dashboard |
| Infraestructura y sistema Base | En curso | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:21 | 18/03/2026 23:40 | Sin fecha | Infraestructura y sistema Base |
| Diseno | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 14/02/2026 16:17 | 18/03/2026 23:40 | 04/03/2026 | Organizacion |
| Cotizacion | Finalizado | software | MAURO ALBERTO RAMOS ANGELES | Medium | 14/02/2026 16:16 | 12/03/2026 00:15 | 18/02/2026 | Organizacion |
| Organizacion | En curso | software | DAVID OLVERA GONZALEZ | Medium | 14/02/2026 16:16 | 18/03/2026 23:40 | 04/03/2026 | Organizacion |

## Observaciones finales para esta actualizacion

1. Se mantiene la misma estructura del documento original y el resumen ya coincide con el estado actual de las actividades en Jira del proyecto KAN.
2. La integracion basica MQTT, la definicion de topicos, la persistencia de datos, las alertas y el dashboard ya quedaron reflejados como actividades finalizadas cuando existe evidencia tecnica suficiente.
3. La parte fisica no se reporta como cerrada; en su lugar se propone una validacion emulada con Raspberry Pi y datasets reales o historicos.
4. El modulo predictivo, el consumo mas amplio de la API desde frontend y algunos pipelines siguen en curso.
5. La autenticacion, login, n8n y la integracion fisica final de sensores se mantienen como pendientes o por hacer.