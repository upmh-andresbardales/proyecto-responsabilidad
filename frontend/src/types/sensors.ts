/**
 * Definiciones de sensores del sistema acuapónico.
 * Configuración centralizada de rangos, unidades y colores.
 */

export interface SensorConfig {
  type: string
  label: string
  unit: string
  gaugeMin: number
  gaugeMax: number
  normalMin: number
  normalMax: number
  criticalLow: number | null
  criticalHigh: number | null
  color: string
  icon: string
  category: 'agua' | 'ambiente' | 'sistema'
}

export const SENSOR_CONFIGS: SensorConfig[] = [
  {
    type: 'ph',
    label: 'pH',
    unit: 'pH',
    gaugeMin: 0,
    gaugeMax: 14,
    normalMin: 6.0,
    normalMax: 8.5,
    criticalLow: 5.5,
    criticalHigh: 9.0,
    color: '#3b82f6',
    icon: '🧪',
    category: 'agua',
  },
  {
    type: 'temperatura_agua',
    label: 'Temp. Agua',
    unit: '°C',
    gaugeMin: 0,
    gaugeMax: 50,
    normalMin: 18,
    normalMax: 30,
    criticalLow: 15,
    criticalHigh: 35,
    color: '#ef4444',
    icon: '🌡️',
    category: 'agua',
  },
  {
    type: 'oxigeno_disuelto',
    label: 'Oxígeno Disuelto',
    unit: 'mg/L',
    gaugeMin: 0,
    gaugeMax: 15,
    normalMin: 5,
    normalMax: 9,
    criticalLow: 4,
    criticalHigh: null,
    color: '#06b6d4',
    icon: '💨',
    category: 'agua',
  },
  {
    type: 'nivel_agua',
    label: 'Nivel de Agua',
    unit: 'cm',
    gaugeMin: 0,
    gaugeMax: 150,
    normalMin: 30,
    normalMax: 100,
    criticalLow: 20,
    criticalHigh: null,
    color: '#8b5cf6',
    icon: '🌊',
    category: 'agua',
  },
  {
    type: 'temperatura_ambiente',
    label: 'Temp. Ambiente',
    unit: '°C',
    gaugeMin: -10,
    gaugeMax: 60,
    normalMin: 15,
    normalMax: 40,
    criticalLow: 10,
    criticalHigh: 45,
    color: '#f59e0b',
    icon: '☀️',
    category: 'ambiente',
  },
  {
    type: 'humedad_ambiente',
    label: 'Humedad',
    unit: '%',
    gaugeMin: 0,
    gaugeMax: 100,
    normalMin: 40,
    normalMax: 80,
    criticalLow: 30,
    criticalHigh: 90,
    color: '#10b981',
    icon: '💧',
    category: 'ambiente',
  },
  {
    type: 'conductividad_electrica',
    label: 'Conductividad',
    unit: 'mS/cm',
    gaugeMin: 0,
    gaugeMax: 6,
    normalMin: 0.5,
    normalMax: 3.0,
    criticalLow: 0.3,
    criticalHigh: 4.0,
    color: '#ec4899',
    icon: '⚡',
    category: 'sistema',
  },
  {
    type: 'turbidez',
    label: 'Turbidez',
    unit: 'NTU',
    gaugeMin: 0,
    gaugeMax: 200,
    normalMin: 0,
    normalMax: 50,
    criticalLow: null,
    criticalHigh: 100,
    color: '#a855f7',
    icon: '🔍',
    category: 'agua',
  },
  {
    type: 'presion_atmosferica',
    label: 'Presión Atm.',
    unit: 'hPa',
    gaugeMin: 850,
    gaugeMax: 1150,
    normalMin: 950,
    normalMax: 1050,
    criticalLow: 900,
    criticalHigh: 1100,
    color: '#64748b',
    icon: '🌤️',
    category: 'ambiente',
  },
  {
    type: 'flujo_agua',
    label: 'Flujo de Agua',
    unit: 'L/min',
    gaugeMin: 0,
    gaugeMax: 20,
    normalMin: 1,
    normalMax: 10,
    criticalLow: 0.5,
    criticalHigh: null,
    color: '#0ea5e9',
    icon: '🚿',
    category: 'sistema',
  },
]

export function getSensorConfig(type: string): SensorConfig | undefined {
  return SENSOR_CONFIGS.find((s) => s.type === type)
}

export function getSensorsByCategory(category: SensorConfig['category']): SensorConfig[] {
  return SENSOR_CONFIGS.filter((s) => s.category === category)
}
