<template>
  <div class="card alert-panel">
    <div v-if="alerts.length === 0" class="no-alerts">
      <span>✅ Sin alertas activas</span>
    </div>
    <div v-else class="alert-list">
      <div
        v-for="(alert, index) in alerts.slice(0, 20)"
        :key="alert.alert_id || index"
        class="alert-item"
        :class="'alert-' + alert.severity"
      >
        <div class="alert-icon">
          {{ alert.severity === 'critical' ? '🔴' : '🟡' }}
        </div>
        <div class="alert-content">
          <div class="alert-message">{{ alert.message }}</div>
          <div class="alert-meta mono">
            <span>{{ alert.sensor_type }}</span>
            <span>{{ formatTime(alert.timestamp) }}</span>
          </div>
        </div>
        <div class="alert-value mono">
          {{ alert.value.toFixed(2) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { AlertData } from '@/composables/useMqtt'

defineProps<{
  alerts: AlertData[]
}>()

function formatTime(timestamp: string): string {
  try {
    return new Date(timestamp).toLocaleTimeString('es-MX')
  } catch {
    return timestamp
  }
}
</script>

<style scoped>
.alert-panel {
  max-height: 400px;
  overflow-y: auto;
}

.no-alerts {
  text-align: center;
  padding: 2rem;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.alert-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.alert-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border-radius: var(--radius-sm);
  border-left: 3px solid transparent;
  transition: background 0.2s;
}

.alert-item:hover {
  background: var(--bg-card-hover);
}

.alert-critical {
  border-left-color: var(--status-critical);
  background: rgba(239, 68, 68, 0.05);
}

.alert-warning {
  border-left-color: var(--status-warning);
  background: rgba(245, 158, 11, 0.05);
}

.alert-icon {
  font-size: 1.2rem;
  flex-shrink: 0;
}

.alert-content {
  flex: 1;
  min-width: 0;
}

.alert-message {
  font-size: 0.85rem;
  color: var(--text-primary);
  margin-bottom: 0.2rem;
}

.alert-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.7rem;
  color: var(--text-muted);
}

.alert-value {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-secondary);
  flex-shrink: 0;
}
</style>
