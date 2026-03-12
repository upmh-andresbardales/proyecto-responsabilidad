<template>
  <div class="dashboard">
    <!-- Header -->
    <header class="dashboard-header">
      <div class="header-left">
        <h1>🌿 Acuaponía Monitor</h1>
        <span class="system-id mono">{{ systemId }}</span>
      </div>
      <div class="header-right">
        <div class="mqtt-status" :class="{ connected: mqttConnected }">
          <span class="status-dot"></span>
          {{ mqttConnected ? 'MQTT Conectado' : 'Desconectado' }}
        </div>
        <span class="timestamp mono">{{ currentTime }}</span>
      </div>
    </header>

    <!-- System Status -->
    <SystemStatus :sensor-data="sensorData" :connected="mqttConnected" />

    <!-- Sensor Gauges Grid -->
    <section class="section">
      <h2 class="section-title">📊 Sensores en Tiempo Real</h2>
      <div class="grid-sensors">
        <SensorGauge
          v-for="sensor in sensorConfig"
          :key="sensor.type"
          :sensor-type="sensor.type"
          :label="sensor.label"
          :unit="sensor.unit"
          :min="sensor.gaugeMin"
          :max="sensor.gaugeMax"
          :normal-min="sensor.normalMin"
          :normal-max="sensor.normalMax"
          :value="sensorData[sensor.type]?.value ?? null"
          :color="sensor.color"
        />
      </div>
    </section>

    <!-- Time Series Charts -->
    <section class="section">
      <h2 class="section-title">📈 Historial Temporal</h2>
      <div class="ts-selector">
        <button
          v-for="sensor in sensorConfig"
          :key="'btn-' + sensor.type"
          class="ts-btn"
          :class="{ active: selectedSensors.includes(sensor.type) }"
          @click="toggleSensor(sensor.type)"
        >
          {{ sensor.icon }} {{ sensor.label }}
        </button>
      </div>
      <div class="grid-charts">
        <SensorTimeSeries
          v-for="sensor in visibleTimeSeries"
          :key="'ts-' + sensor.type"
          :sensor-type="sensor.type"
          :label="sensor.label"
          :unit="sensor.unit"
          :color="sensor.color"
          :current-value="sensorData[sensor.type]?.value ?? null"
          :normal-min="sensor.normalMin"
          :normal-max="sensor.normalMax"
        />
      </div>
    </section>

    <!-- Alerts Panel -->
    <section class="section">
      <h2 class="section-title">
        🚨 Alertas
        <span v-if="alerts.length" class="badge badge-critical">{{ alerts.length }}</span>
      </h2>
      <AlertPanel :alerts="alerts" />
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useMqtt } from '@/composables/useMqtt'
import SensorGauge from '@/components/SensorGauge.vue'
import SensorTimeSeries from '@/components/SensorTimeSeries.vue'
import AlertPanel from '@/components/AlertPanel.vue'
import SystemStatus from '@/components/SystemStatus.vue'
import { SENSOR_CONFIGS } from '@/types/sensors'

const systemId = import.meta.env.VITE_SYSTEM_ID || 'sistema-01'
const { connected: mqttConnected, sensorData, alerts, connect } = useMqtt()

const currentTime = ref('')
let timeInterval: ReturnType<typeof setInterval>

const sensorConfig = SENSOR_CONFIGS

// Sensor selection for time series
const selectedSensors = ref(['ph', 'temperatura_agua', 'oxigeno_disuelto', 'flujo_agua'])

const visibleTimeSeries = computed(() =>
  sensorConfig.filter((s) => selectedSensors.value.includes(s.type))
)

function toggleSensor(type: string) {
  const idx = selectedSensors.value.indexOf(type)
  if (idx >= 0) {
    selectedSensors.value.splice(idx, 1)
  } else {
    selectedSensors.value.push(type)
  }
}

function updateTime() {
  currentTime.value = new Date().toLocaleString('es-MX', {
    dateStyle: 'medium',
    timeStyle: 'medium',
  })
}

onMounted(() => {
  connect()
  updateTime()
  timeInterval = setInterval(updateTime, 1000)
})

onUnmounted(() => {
  clearInterval(timeInterval)
})
</script>

<style scoped>
.dashboard {
  max-width: 1600px;
  margin: 0 auto;
  padding: 1.5rem;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow-md);
}

.header-left h1 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.system-id {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.mqtt-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: var(--status-critical);
}

.mqtt-status.connected {
  color: var(--status-normal);
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--status-critical);
  animation: pulse 2s infinite;
}

.connected .status-dot {
  background: var(--status-normal);
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.timestamp {
  font-size: 0.8rem;
  color: var(--text-secondary);
}

.section {
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.grid-charts {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(480px, 1fr));
  gap: 1rem;
}

.ts-selector {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1rem;
}

.ts-btn {
  padding: 0.3rem 0.7rem;
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  background: var(--bg-card);
  color: var(--text-muted);
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}

.ts-btn:hover {
  border-color: var(--accent-blue);
  color: var(--text-primary);
}

.ts-btn.active {
  background: rgba(59, 130, 246, 0.15);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}

@media (max-width: 768px) {
  .dashboard-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .header-right {
    flex-direction: column;
    gap: 0.5rem;
  }

  .grid-charts {
    grid-template-columns: 1fr;
  }
}
</style>
