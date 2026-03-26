# Investigación: Condiciones Óptimas en Hidroponía y Acuaponía

**Equipo:** OptiMind Four  
**Materia:** Responsabilidad Social — Maestría en Inteligencia Artificial  
**Fecha:** 2026-03-25

---

## 1. Introducción

La acuaponía es un sistema integrado que combina acuicultura (cría de peces) con hidroponía (cultivo de plantas sin suelo) en un ciclo simbiótico. Los desechos de los peces proporcionan nutrientes a las plantas, y las plantas filtran el agua para los peces.

El monitoreo continuo de variables ambientales es esencial para mantener el equilibrio del sistema y maximizar la producción. Este documento resume las condiciones óptimas basadas en literatura científica y las relaciona con los sensores implementados en la plataforma.

---

## 2. Variables Críticas y Rangos Óptimos

### 2.1 pH del Agua

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 6.0 – 7.0 (compromiso entre peces y plantas) |
| Rango aceptable | 6.0 – 8.5 |
| Rango crítico | < 5.5 o > 9.0 |

**Justificación:** En acuaponía, el pH ideal es un compromiso entre las necesidades de los peces (7.0–8.0), las plantas (5.5–6.5) y las bacterias nitrificantes (7.0–8.0). Un rango de 6.0–7.0 es ampliamente aceptado como el punto óptimo de compromiso (Rakocy et al., 2006; Somerville et al., 2014).

**Impacto fuera de rango:**
- pH bajo (< 6.0): Estrés en peces, inhibición de bacterias nitrificantes.
- pH alto (> 8.5): Toxicidad por amoniaco no ionizado, deficiencias nutricionales en plantas.

### 2.2 Temperatura del Agua

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 22 – 28 °C |
| Rango aceptable | 18 – 30 °C |
| Rango crítico | < 15 o > 35 °C |

**Justificación:** La temperatura del agua afecta directamente el metabolismo de los peces, la actividad bacteriana y la absorción de nutrientes por las raíces. La tilapia, especie común en acuaponía, prospera entre 22–28 °C (FAO, 2014).

**Impacto fuera de rango:**
- Agua fría (< 18 °C): Reducción del metabolismo, menor crecimiento.
- Agua caliente (> 30 °C): Reducción de oxígeno disuelto, estrés térmico.

### 2.3 Oxígeno Disuelto (OD)

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 5.0 – 8.0 mg/L |
| Mínimo aceptable | 5.0 mg/L |
| Nivel crítico | < 4.0 mg/L |

**Justificación:** El oxígeno disuelto es el parámetro más crítico en acuaponía. Los peces requieren al menos 5 mg/L para respiración adecuada, y las bacterias nitrificantes necesitan oxígeno para convertir amoniaco en nitrato (Timmons & Ebeling, 2013).

**Impacto fuera de rango:**
- OD bajo (< 4.0 mg/L): Mortalidad de peces, colapso de la nitrificación.

### 2.4 Nivel de Agua

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 40 – 80 cm (según diseño del tanque) |
| Mínimo aceptable | 30 cm |
| Nivel crítico | < 20 cm |

**Justificación:** El nivel de agua garantiza que las raíces de las plantas estén sumergidas en el medio nutriente y que los peces tengan volumen suficiente para nadar. Un nivel bajo indica posible fuga o falla en la bomba.

### 2.5 Temperatura Ambiente

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 20 – 35 °C |
| Rango aceptable | 15 – 40 °C |
| Rango crítico | < 10 o > 45 °C |

**Justificación:** La temperatura ambiente influye directamente en la temperatura del agua y en la tasa de evapotranspiración de las plantas. En climas tropicales y subtropicales como México, la acuaponía se beneficia de temperaturas cálidas estables (Somerville et al., 2014).

### 2.6 Humedad Ambiente

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 50 – 70 % |
| Rango aceptable | 40 – 80 % |
| Rango crítico | < 30 o > 90 % |

**Justificación:** La humedad relativa controla la transpiración de las plantas. Humedad muy baja acelera la pérdida de agua; muy alta favorece hongos y enfermedades foliares.

### 2.7 Conductividad Eléctrica (EC)

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 0.8 – 2.0 mS/cm |
| Rango aceptable | 0.5 – 3.0 mS/cm |
| Rango crítico | < 0.3 o > 4.0 mS/cm |

**Justificación:** La EC refleja la concentración total de sales y nutrientes disueltos. En acuaponía, la EC tiende a ser menor que en hidroponía pura porque los nutrientes provienen del metabolismo de los peces (Goddek et al., 2019).

### 2.8 Turbidez

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 0 – 25 NTU |
| Rango aceptable | 0 – 50 NTU |
| Rango crítico | > 100 NTU |

**Justificación:** La turbidez indica la cantidad de partículas suspendidas (alimento no consumido, heces, algas). Turbidez alta reduce la penetración de luz y puede obstruir filtros y raíces.

### 2.9 Presión Atmosférica

| Parámetro | Valor |
|-----------|-------|
| Rango normal | 950 – 1050 hPa |
| Rango aceptable | 900 – 1100 hPa |

**Justificación:** La presión atmosférica afecta la solubilidad del oxígeno en agua. A mayor altitud (menor presión), menor concentración de OD en equilibrio. En la zona metropolitana de Hidalgo (~2400 msnm), la presión típica es ~760 mmHg (~1013 hPa ajustado), lo que reduce la capacidad natural de OD y hace más crítico el monitoreo de oxígeno disuelto.

### 2.10 Flujo de Agua

| Parámetro | Valor |
|-----------|-------|
| Rango óptimo | 2 – 8 L/min (según escala) |
| Mínimo aceptable | 1.0 L/min |
| Nivel crítico | < 0.5 L/min |

**Justificación:** El flujo de agua asegura la circulación entre el tanque de peces y las camas de cultivo. Un flujo insuficiente reduce el transporte de nutrientes y oxígeno. Un flujo excesivo puede dañar raíces y generar estrés en los peces (Lennard & Leonard, 2006).

---

## 3. Relación entre Sensores y el Sistema

| Sensor del Sistema | Variable Monitoreada | Impacto en el Ecosistema |
|--------------------|---------------------|--------------------------|
| ph-01 | pH del agua | Salud de peces, disponibilidad de nutrientes, actividad bacteriana |
| temp-agua-01 | Temperatura del agua | Metabolismo de peces, nitrificación, absorción radicular |
| od-01 | Oxígeno disuelto | Respiración de peces, nitrificación aeróbica |
| nivel-01 | Nivel de agua | Integridad del sistema, cobertura de raíces |
| temp-amb-01 | Temperatura ambiente | Regulación térmica indirecta, evapotranspiración |
| hum-01 | Humedad ambiente | Transpiración, riesgo de enfermedades foliares |
| ce-01 | Conductividad eléctrica | Concentración de nutrientes disueltos |
| turb-01 | Turbidez | Salud del agua, eficiencia de filtración |
| pres-01 | Presión atmosférica | Solubilidad de oxígeno, contexto ambiental |
| flujo-01 | Flujo de agua | Circulación de nutrientes, salud de la bomba |

---

## 4. Umbrales Implementados en el Sistema

Los umbrales del archivo `mqtt_client.py` del backend coinciden con los rangos documentados aquí, validados contra la literatura:

| Sensor | Warning Low | Warning High | Critical Low | Critical High |
|--------|------------|-------------|-------------|--------------|
| pH | 6.0 | 8.5 | 5.5 | 9.0 |
| Temp. Agua | 18.0 | 30.0 | 15.0 | 35.0 |
| Oxígeno Disuelto | 5.0 | 9.0 | 4.0 | — |
| Nivel Agua | 30.0 | 100.0 | 20.0 | — |
| Temp. Ambiente | 15.0 | 40.0 | 10.0 | 45.0 |
| Humedad | 40.0 | 80.0 | 30.0 | 90.0 |
| Conductividad | 0.5 | 3.0 | 0.3 | 4.0 |
| Turbidez | — | 50.0 | — | 100.0 |
| Presión Atm. | 950.0 | 1050.0 | 900.0 | 1100.0 |
| Flujo Agua | 1.0 | 10.0 | 0.5 | — |

---

## 5. Referencias

- FAO. (2014). *Small-scale aquaponic food production*. FAO Fisheries and Aquaculture Technical Paper No. 589.
- Goddek, S., et al. (2019). *Aquaponics Food Production Systems*. Springer Open.
- Lennard, W. A., & Leonard, B. V. (2006). A comparison of three different hydroponic sub-systems (gravel, floating and nutrient film technique) in an aquaponic test system. *Aquaculture International*, 14(6), 539–550.
- Rakocy, J. E., Masser, M. P., & Losordo, T. M. (2006). Recirculating aquaculture tank production systems: Aquaponics — integrating fish and plant culture. *SRAC Publication*, 454.
- Somerville, C., Cohen, M., Pantanella, E., Stankus, A., & Lovatelli, A. (2014). *Small-scale aquaponic food production*. FAO.
- Timmons, M. B., & Ebeling, J. M. (2013). *Recirculating Aquaculture*. Ithaca, NY: Cayuga Aqua Ventures.
