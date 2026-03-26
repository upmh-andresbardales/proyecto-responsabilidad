# Universidad Politecnica Metropolitana de Hidalgo

## Carrera: Maestria en Inteligencia Artificial

### CUATRIMESTRE 2

Grupo: Unico  
Nombre del Equipo: OptiMind Four  
Docente: Dr. Victor Dario Cuervo Pinto  
Materia: Responsabilidad Social

### Integrantes

Bardales Calva Jose Andres 253220002  
Martin Lopez Misael 253220165  
Olvera Gonzalez David 253220060  
Ramos Angeles Mauro Alberto 253220121

# Monitoreo y control

Documento actualizado con base en el avance real del proyecto y en el estado actual de las actividades registradas en Jira al 2026-03-18.

## Actividad 1 - Analisis de los indicadores de actividades y componentes

| Actividad | Indicador | Meta | Resultado actual | Cumplimiento | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1. Configurar orquestacion Docker y pipelines de despliegue | Sistema de contenedores configurado y funcionando | Plataforma operativa en entorno local | Orquestacion Docker funcional, despliegue remoto automatizado basico y servicios principales levantados | Alto | Permite desplegar la plataforma del sistema y ya existe base de despliegue local y en nube |
| 2. Ensamblar la unidad piloto fisica y calibrar sensores | Nodo sensor funcional o flujo de adquisicion validado | Unidad piloto de hidroponia con sensores operativos o fuente equivalente validada | La parte fisica completa sigue pendiente; se trabaja con simulacion y se propone validacion emulada con Raspberry Pi y datasets reales o historicos | Medio | Reduce la dependencia de sensores fisicos en esta etapa y permite validar integracion |
| 3. Desarrollar API de clima e integracion con modelo Keras | API conectada con el sistema y modulo predictivo disponible | Integracion de datos del sistema y modelo IA | Backend funcional con endpoints de consulta y prediccion; el modelo final aun no esta integrado | Medio | Requiere pruebas con datos reales o historicos e integracion del modelo definitivo |
| 4. Implementar Job Cron para generacion de datos sinteticos | Automatizacion de generacion de datos | Sistema capaz de simular datos para pruebas | Existe un servicio funcional de datos sinteticos por MQTT; la automatizacion opera de manera continua | Alto | Permite pruebas sin depender de sensores reales |

## Actividad 3 - Probabilidad de logro de los objetivos del proyecto

| Nivel del proyecto | Objetivo | Situacion actual | Probabilidad de logro | Justificacion |
| --- | --- | --- | --- | --- |
| Fin | Contribuir a la soberania alimentaria urbana mediante tecnologia de hidroponia inteligente | Desarrollo de plataforma open source funcional de monitoreo, persistencia, visualizacion y simulacion | Alta | El sistema ya cuenta con componentes principales operativos y una arquitectura replicable |
| Proposito | Implementar una plataforma tecnologica que optimice el cultivo hidroponico | Desarrollo del software principal en funcionamiento; validacion emulada de adquisicion y consolidacion del modulo predictivo en curso | Alta | El proyecto combina software, mensajeria, persistencia, visualizacion e IA en una sola plataforma |
| Componentes | Sistema de monitoreo, control automatizado y modelo predictivo | Monitoreo en tiempo real, persistencia, alertas y dashboard ya implementados; adquisicion emulada y modelo final en progreso | Media-Alta | Algunas partes aun dependen de integracion avanzada, datos reales y validacion final |

## Actividad 4 - Problemas y acciones

| Problema identificado | Causa | Impacto en el proyecto | Accion correctiva | Responsable |
| --- | --- | --- | --- | --- |
| Disponibilidad de sensores electronicos | Mercado local limitado | Retraso en pruebas del sistema fisico | Buscar proveedores alternativos y mantener simulacion o emulacion de datos como respaldo | Equipo de hardware |
| Integracion entre software y hardware | Diferencias en protocolos y comunicacion | Posible retraso en pruebas del sistema | Implementar pruebas con datos sinteticos y validacion emulada con Raspberry Pi | Equipo de desarrollo |
| Validacion del modelo de IA | Necesidad de suficientes datos | Limitacion en entrenamiento del modelo | Generar datos simulados, aprovechar datasets externos y preparar integracion del modelo final | Equipo de IA |

## Actividad 1 - Configuracion del sistema

| Elemento | Descripcion |
| --- | --- |
| Indicador | Plataforma Docker funcionando |
| Meta | Sistema desplegado en entorno local |
| Medio de verificacion | Pruebas de ejecucion del sistema, despliegue de servicios y funcionamiento del dashboard |
| Supuestos | Disponibilidad de infraestructura y software |

## Actividad 2 - Unidad piloto

| Elemento | Descripcion |
| --- | --- |
| Indicador | Fuente de datos validada, fisica o emulada |
| Meta | Sistema piloto capaz de recibir datos equivalentes a una lectura real |
| Medio de verificacion | Lecturas publicadas por MQTT, persistidas en backend y visibles en dashboard |
| Supuestos | Disponibilidad de componentes electronicos o de Raspberry Pi y datasets reales adaptables |

## Actividad 3 - Integracion de IA y API

| Elemento | Descripcion |
| --- | --- |
| Indicador | API funcional y modulo de prediccion integrado a nivel operativo |
| Meta | Sistema capaz de generar predicciones y consultas utiles para monitoreo |
| Medio de verificacion | Resultados de endpoints y respuestas del servicio de prediccion |
| Supuestos | Disponibilidad de datos suficientes |

## Actividad 4 - Datos sinteticos

| Elemento | Descripcion |
| --- | --- |
| Indicador | Generacion automatica de datos |
| Meta | Simulacion continua de datos para pruebas |
| Medio de verificacion | Registros del sistema, publicaciones MQTT y visualizacion en frontend |
| Supuestos | Correcta programacion del servicio de generacion y disponibilidad del broker MQTT |

## Resumen actualizado de actividades

| Resumen | Estado | Tipo de proyecto | Persona asignada | Prioridad | Creada | Actualizada | Fecha de vencimiento | Parent summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Organizacion | En curso | software | DAVID OLVERA GONZALEZ | Medium | 14/02/2026 16:16 | 18/03/2026 23:40 | 04/03/2026 | Organizacion |
| Cotizacion | Finalizado | software | MAURO ALBERTO RAMOS ANGELES | Medium | 14/02/2026 16:16 | 12/03/2026 00:15 | 18/02/2026 | Organizacion |
| Diseno | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 14/02/2026 16:17 | 18/03/2026 23:40 | 04/03/2026 | Organizacion |
| Infraestructura y sistema Base | En curso | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:21 | 18/03/2026 23:40 | Sin fecha | Infraestructura y sistema Base |
| Frontend Dashboard | En curso | software | JOSE ANDRES BARDALES CALVA | Medium | 24/02/2026 21:22 | 18/03/2026 22:54 | 03/04/2026 | Frontend Dashboard |
| Crear diseno inicial o bosquejo | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:22 | 18/03/2026 23:41 | 04/03/2026 | Frontend Dashboard |
| Construir el esquelo en vuejs | Finalizado | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:23 | 18/03/2026 23:41 | 08/03/2026 | Frontend Dashboard |
| Construir login | Por hacer | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:23 | 18/03/2026 23:41 | 13/03/2026 | Frontend Dashboard |
| Backend | En curso | software | MISAEL MARTIN LOPEZ | Medium | 24/02/2026 21:23 | 18/03/2026 22:54 | 11/04/2026 | Backend |
| Configurar Servidor MQTT | Finalizado | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:23 | 18/03/2026 23:01 | Sin fecha | Backend |
| Conectar frontend con endpoints de backend | En curso | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:24 | 18/03/2026 23:09 | 20/03/2026 | Frontend Dashboard |
| Conectar con mqtt(emqx) | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:24 | 18/03/2026 23:41 | 01/04/2026 | Frontend Dashboard |
| generar servicio para datos sinteticos (n8n o fastapi) | En curso | software | MAURO ALBERTO RAMOS ANGELES | Medium | 24/02/2026 21:24 | 18/03/2026 23:41 | 04/04/2026 | Datos sinteticos |
| Investigacion condiciones optimas en hidroponia | Por hacer | software | JOSE ANDRES BARDALES CALVA | Medium | 24/02/2026 21:26 | 12/03/2026 00:22 | 08/04/2026 | Investigacion |
| Configurar persistencia y gestion de datos en MongoDB | En curso | software | DAVID OLVERA GONZALEZ | Medium | 24/02/2026 21:31 | 18/03/2026 23:48 | Sin fecha | Base Datos |
| Crear instancia AWS | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:18 | 18/03/2026 23:09 | 19/03/2026 | Infraestructura y sistema Base |
| Configrar plataforma base para lanzamiento de aplicaciones | Finalizado | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:19 | 18/03/2026 23:09 | 01/04/2026 | Infraestructura y sistema Base |
| Lanzamiento de frontend | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:41 | 26/03/2026 | Infraestructura y sistema Base |
| Lanzamiento de backend fast api | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:42 | 03/04/2026 | Infraestructura y sistema Base |
| Lanzamiento Mongo DB | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:42 | 03/04/2026 | Infraestructura y sistema Base |
| Lanzamiento EMQX | Finalizado | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:19 | 18/03/2026 23:42 | 04/04/2026 | Infraestructura y sistema Base |
| Lanzamiento n8n para trabajar con agentes | Por hacer | software | MAURO ALBERTO RAMOS ANGELES | Medium | 27/02/2026 00:20 | 12/03/2026 00:19 | 04/04/2026 | Infraestructura y sistema Base |
| Configurar y probar pipeline de despliege FRONT | En curso | software | MAURO ALBERTO RAMOS ANGELES | Medium | 27/02/2026 00:20 | 18/03/2026 23:42 | 02/04/2026 | Frontend Dashboard |
| Modelo relacional | Por hacer | software | DAVID OLVERA GONZALEZ | Medium | 27/02/2026 00:21 | 12/03/2026 00:22 | 02/04/2026 | Base Datos |
| Configurar y probar pipeline de despliege (backend) | En curso | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:21 | 18/03/2026 23:42 | 07/04/2026 | Backend |
| CRUD usuarios y login | Por hacer | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:21 | 18/03/2026 23:41 | 03/04/2026 | Backend |
| CRUD historial de lectura de sensores | En curso | software | JOSE ANDRES BARDALES CALVA | Medium | 27/02/2026 00:22 | 18/03/2026 23:41 | 11/04/2026 | Backend |
| Funcion suscrita a topicos mqtt para registrar sensores en BD | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:22 | 18/03/2026 23:41 | 11/04/2026 | Backend |
| Funcion subscrita a topicos mqtt para alarmas y alertas | Finalizado | software | MISAEL MARTIN LOPEZ | Medium | 27/02/2026 00:23 | 18/03/2026 23:41 | 10/04/2026 | Backend |

## Observaciones finales

1. La estructura de este documento conserva el formato de la primera entrega.
2. Los estados del resumen fueron actualizados directamente con base en Jira y alineados al avance real del proyecto.
3. La integracion MQTT, la persistencia de datos, las alertas, MongoDB operativo, el backend base y el frontend base ya cuentan con evidencia funcional.
4. La parte fisica se mantiene como validacion pendiente o emulada, sin reportarla como cerrada.
5. Las tareas de autenticacion, n8n, modelo relacional y cierre del modulo predictivo continúan pendientes o en progreso segun corresponda.