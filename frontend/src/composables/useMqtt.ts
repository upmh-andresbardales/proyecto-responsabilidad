/**
 * Composable MQTT - Conexión a EMQX vía WebSocket
 * Gestiona la suscripción a tópicos de sensores y alertas.
 */

import { ref, reactive, onUnmounted } from 'vue'
import mqtt, { type MqttClient } from 'mqtt'

export interface SensorData {
  sensor_id: string
  value: number
  unit: string
  timestamp: string
  system_id: string
}

export interface AlertData {
  alert_id: string
  sensor_type: string
  sensor_id: string
  value: number
  threshold: number
  severity: 'warning' | 'critical'
  message: string
  timestamp: string
  system_id: string
}

// Configuración MQTT - usa la IP del browser para producción
function getMqttUrl(): string {
  if (import.meta.env.VITE_MQTT_URL) return import.meta.env.VITE_MQTT_URL
  const host = window.location.hostname
  const port = 8084
  return `ws://${host}:${port}/mqtt`
}

const MQTT_URL = getMqttUrl()
const SYSTEM_ID = import.meta.env.VITE_SYSTEM_ID || 'sistema-01'
const BASE_TOPIC = import.meta.env.VITE_MQTT_BASE_TOPIC || 'acuaponia'

// Estado global compartido
const connected = ref(false)
const sensorData = reactive<Record<string, SensorData>>({})
const alerts = ref<AlertData[]>([])
let client: MqttClient | null = null
let initialized = false

export function useMqtt() {
  function connect() {
    if (initialized && client?.connected) return

    console.log(`[MQTT] Conectando a ${MQTT_URL}...`)

    client = mqtt.connect(MQTT_URL, {
      clientId: `vue-dashboard-${Math.random().toString(16).slice(2, 8)}`,
      clean: true,
      connectTimeout: 5000,
      reconnectPeriod: 3000,
    })

    client.on('connect', () => {
      connected.value = true
      console.log('[MQTT] Conectado exitosamente')

      // Suscribirse a todos los sensores
      const sensorTopic = `${BASE_TOPIC}/+/sensor/+/data`
      const alertTopic = `${BASE_TOPIC}/+/alert`

      client!.subscribe([sensorTopic, alertTopic], { qos: 1 }, (err) => {
        if (err) {
          console.error('[MQTT] Error en suscripcion:', err)
        } else {
          console.log(`[MQTT] Suscrito a: ${sensorTopic}, ${alertTopic}`)
        }
      })
    })

    client.on('message', (topic, message) => {
      try {
        const payload = JSON.parse(message.toString())
        const parts = topic.split('/')

        if (topic.includes('/sensor/') && topic.endsWith('/data')) {
          // Es dato de sensor: acuaponia/{system_id}/sensor/{sensor_type}/data
          const sensorType = parts[3]
          sensorData[sensorType] = payload
        } else if (topic.endsWith('/alert')) {
          // Es alerta
          alerts.value.unshift(payload)
          // Mantener solo las últimas 100 alertas en memoria
          if (alerts.value.length > 100) {
            alerts.value = alerts.value.slice(0, 100)
          }
        }
      } catch (e) {
        console.error('[MQTT] Error parseando mensaje:', e)
      }
    })

    client.on('error', (err) => {
      console.error('[MQTT] Error:', err)
    })

    client.on('close', () => {
      connected.value = false
      console.log('[MQTT] Desconectado')
    })

    client.on('reconnect', () => {
      console.log('[MQTT] Reconectando...')
    })

    initialized = true
  }

  function disconnect() {
    if (client) {
      client.end()
      connected.value = false
      initialized = false
      console.log('[MQTT] Desconectado manualmente')
    }
  }

  return {
    connected,
    sensorData,
    alerts,
    connect,
    disconnect,
  }
}
