<template>
  <div class="card gauge-card" :class="statusClass">
    <div class="gauge-header">
      <span class="gauge-label">{{ label }}</span>
      <span class="gauge-value mono" :style="{ color: statusHex }">
        {{ displayValue }}
        <small>{{ unit }}</small>
      </span>
    </div>
    <v-chart class="gauge-chart" :option="gaugeOption" autoresize />
    <div class="gauge-range">
      <span>{{ min }}</span>
      <span class="range-normal">{{ normalMin }} – {{ normalMax }}</span>
      <span>{{ max }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import VChart from 'vue-echarts'

// Colores fijos (ECharts no soporta CSS variables)
const COLOR_NORMAL = '#10b981'
const COLOR_WARNING = '#f59e0b'
const COLOR_CRITICAL = '#ef4444'
const COLOR_MUTED = '#64748b'
const COLOR_TRACK = '#1e293b'

const props = defineProps<{
  sensorType: string
  label: string
  unit: string
  min: number
  max: number
  normalMin: number
  normalMax: number
  value: number | null
  color: string
}>()

const displayValue = computed(() =>
  props.value !== null ? props.value.toFixed(2) : '--'
)

/** Hex color based on sensor status — usable by ECharts */
const statusHex = computed(() => {
  if (props.value === null) return COLOR_MUTED
  if (props.value < props.normalMin || props.value > props.normalMax) {
    // check if beyond 15% outside of normal range → critical
    const range = props.normalMax - props.normalMin
    const margin = range * 0.3
    if (
      props.value < props.normalMin - margin ||
      props.value > props.normalMax + margin
    ) {
      return COLOR_CRITICAL
    }
    return COLOR_WARNING
  }
  return COLOR_NORMAL
})

const statusClass = computed(() => {
  if (props.value === null) return ''
  if (statusHex.value === COLOR_CRITICAL) return 'status-critical'
  if (statusHex.value === COLOR_WARNING) return 'status-warning'
  return ''
})

/** Compute zone boundaries as fractions of the full gauge range */
const zones = computed(() => {
  const total = props.max - props.min
  const normalStart = (props.normalMin - props.min) / total
  const normalEnd = (props.normalMax - props.min) / total
  return [
    [normalStart, COLOR_CRITICAL + '55'],    // below normal
    [normalEnd, COLOR_NORMAL + '55'],        // normal zone
    [1, COLOR_CRITICAL + '55'],              // above normal
  ] as [number, string][]
})

const gaugeOption = computed(() => ({
  series: [
    {
      type: 'gauge',
      min: props.min,
      max: props.max,
      startAngle: 220,
      endAngle: -40,
      radius: '90%',
      // Colored zone track
      axisLine: {
        lineStyle: {
          width: 16,
          color: zones.value,
        },
      },
      // Progress fill from 0 to current value
      progress: {
        show: true,
        width: 16,
        roundCap: true,
        itemStyle: {
          color: {
            type: 'linear',
            x: 0, y: 0, x2: 1, y2: 0,
            colorStops: [
              { offset: 0, color: statusHex.value + 'aa' },
              { offset: 1, color: statusHex.value },
            ],
          },
        },
      },
      // Pointer needle
      pointer: {
        show: true,
        length: '55%',
        width: 4,
        offsetCenter: [0, 0],
        itemStyle: {
          color: statusHex.value,
          shadowColor: statusHex.value + '80',
          shadowBlur: 8,
        },
      },
      anchor: {
        show: true,
        size: 8,
        showAbove: true,
        itemStyle: {
          color: statusHex.value,
          borderWidth: 2,
          borderColor: '#0f172a',
        },
      },
      axisTick: {
        show: true,
        splitNumber: 5,
        length: 4,
        lineStyle: { color: '#475569', width: 1 },
      },
      splitLine: {
        show: true,
        length: 8,
        lineStyle: { color: '#475569', width: 1.5 },
      },
      axisLabel: {
        show: false,
      },
      title: { show: false },
      detail: {
        valueAnimation: true,
        fontSize: 22,
        fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
        fontWeight: 700,
        color: statusHex.value,
        offsetCenter: [0, '65%'],
        formatter: (val: number) =>
          props.value !== null ? `${val.toFixed(1)} ${props.unit}` : '--',
      },
      data: [{ value: props.value ?? props.min }],
      animationDuration: 800,
      animationEasingUpdate: 'cubicOut',
    },
  ],
}))
</script>

<style scoped>
.gauge-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  min-height: 280px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.gauge-card.status-critical {
  border-color: #ef444460;
  box-shadow: 0 0 12px #ef444425;
}

.gauge-card.status-warning {
  border-color: #f59e0b50;
  box-shadow: 0 0 12px #f59e0b20;
}

.gauge-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 0;
}

.gauge-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.gauge-value {
  font-size: 1.1rem;
  font-weight: 700;
}

.gauge-value small {
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-left: 2px;
}

.gauge-chart {
  width: 100%;
  height: 200px;
}

.gauge-range {
  display: flex;
  justify-content: space-between;
  width: 85%;
  font-size: 0.65rem;
  color: var(--text-muted);
  margin-top: -8px;
  font-family: 'JetBrains Mono', monospace;
}

.range-normal {
  color: #10b981;
  font-weight: 600;
}
</style>
