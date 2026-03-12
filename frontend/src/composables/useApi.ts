/**
 * API Client - Axios configurado para el backend FastAPI.
 */

import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_URL || '/api'

const api = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Tipos de respuesta
export interface SensorReading {
  sensor_id: string
  sensor_type: string
  value: number
  unit: string
  timestamp: string
  system_id: string
}

export interface AlertResponse {
  alert_id: string
  sensor_type: string
  sensor_id: string
  value: number
  threshold: number
  severity: string
  message: string
  timestamp: string
  system_id: string
  acknowledged: boolean
}

export interface SensorStats {
  sensor_type: string
  avg: number
  min: number
  max: number
  count: number
  last_value: number | null
  last_timestamp: string | null
}

export interface AlertCount {
  total: number
  critical: number
  warning: number
}

export interface PredictionRequest {
  ph: number
  temperatura_agua: number
  oxigeno_disuelto: number
  nivel_agua: number
  temperatura_ambiente: number
  humedad_ambiente: number
  conductividad_electrica: number
  turbidez: number
  presion_atmosferica: number
  flujo_agua: number
}

export interface PredictionResponse {
  prediction: string
  confidence: number
  recommendations: string[]
  model_version: string
}

// Endpoints
export const sensorsApi = {
  getLatest: () => api.get<SensorReading[]>('/sensors/latest'),
  getHistory: (sensorType: string, minutes = 60, limit = 200) =>
    api.get<SensorReading[]>(`/sensors/${sensorType}/history`, {
      params: { minutes, limit },
    }),
  getStats: (minutes = 60) =>
    api.get<SensorStats[]>('/sensors/stats', { params: { minutes } }),
}

export const alertsApi = {
  getAlerts: (limit = 50, severity?: string) =>
    api.get<AlertResponse[]>('/alerts', { params: { limit, severity } }),
  getCount: () => api.get<AlertCount>('/alerts/count'),
}

export const predictionApi = {
  predict: (data: PredictionRequest) =>
    api.post<PredictionResponse>('/predict', data),
}

export default api
