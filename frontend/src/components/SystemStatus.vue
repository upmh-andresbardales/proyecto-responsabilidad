<template>
  <div class="card system-status">
    <div class="status-grid">
      <div class="status-item">
        <span class="status-label">Sensores Activos</span>
        <span class="status-value mono" :style="{ color: activeSensors > 0 ? 'var(--status-normal)' : 'var(--status-critical)' }">
          {{ activeSensors }}/10
        </span>
      </div>
      <div class="status-item">
        <span class="status-label">Conexión MQTT</span>
        <span class="status-value" :class="connected ? 'badge-normal' : 'badge-critical'" style="padding: 0.2rem 0.6rem; border-radius: 9999px; font-size: 0.8rem;">
          {{ connected ? '● Online' : '● Offline' }}
        </span>
      </div>
      <div class="status-item">
        <span class="status-label">Última Lectura</span>
        <span class="status-value mono">{{ lastUpdate }}</span>
      </div>
      <div class="status-item">
        <span class="status-label">Estado General</span>
        <span class="status-value" :class="overallStatusClass">
          {{ overallStatus }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { SensorData } from '@/composables/useMqtt'

const props = defineProps<{
  sensorData: Record<string, SensorData>
  connected: boolean
}>()

const activeSensors = computed(() => Object.keys(props.sensorData).length)

const lastUpdate = computed(() => {
  const timestamps = Object.values(props.sensorData).map((s) => new Date(s.timestamp).getTime())
  if (timestamps.length === 0) return 'Sin datos'
  const latest = new Date(Math.max(...timestamps))
  return latest.toLocaleTimeString('es-MX')
})

const overallStatus = computed(() => {
  if (!props.connected) return 'Desconectado'
  if (activeSensors.value === 0) return 'Sin datos'
  if (activeSensors.value < 10) return 'Parcial'
  return 'Operando'
})

const overallStatusClass = computed(() => {
  if (!props.connected || activeSensors.value === 0) return 'badge badge-critical'
  if (activeSensors.value < 10) return 'badge badge-warning'
  return 'badge badge-normal'
})
</script>

<style scoped>
.system-status {
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, var(--bg-card) 0%, rgba(59, 130, 246, 0.05) 100%);
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.5rem;
}

.status-item {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.status-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-value {
  font-size: 1.1rem;
  font-weight: 600;
}
</style>
