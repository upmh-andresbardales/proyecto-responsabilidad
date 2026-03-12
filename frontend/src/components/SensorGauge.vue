<template>
  <div class="card gauge-card">
    <div class="gauge-header">
      <span class="gauge-label">{{ label }}</span>
      <span class="gauge-value mono" :style="{ color: statusColor }">
        {{ displayValue }}
        <small>{{ unit }}</small>
      </span>
    </div>
    <v-chart class="gauge-chart" :option="gaugeOption" autoresize />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import VChart from 'vue-echarts'

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

const statusColor = computed(() => {
  if (props.value === null) return 'var(--text-muted)'
  if (props.value < props.normalMin || props.value > props.normalMax) {
    return 'var(--status-critical)'
  }
  const range = props.normalMax - props.normalMin
  const margin = range * 0.15
  if (
    props.value < props.normalMin + margin ||
    props.value > props.normalMax - margin
  ) {
    return 'var(--status-warning)'
  }
  return 'var(--status-normal)'
})

const gaugeOption = computed(() => ({
  series: [
    {
      type: 'gauge',
      min: props.min,
      max: props.max,
      startAngle: 220,
      endAngle: -40,
      radius: '85%',
      progress: {
        show: true,
        width: 14,
        roundCap: true,
        itemStyle: {
          color: props.value !== null ? statusColor.value : '#333',
        },
      },
      axisLine: {
        lineStyle: {
          width: 14,
          color: [[1, '#2d3748']],
        },
      },
      axisTick: { show: false },
      splitLine: { show: false },
      axisLabel: {
        distance: 20,
        fontSize: 10,
        color: '#64748b',
      },
      pointer: { show: false },
      anchor: { show: false },
      title: { show: false },
      detail: {
        valueAnimation: true,
        fontSize: 24,
        fontFamily: 'JetBrains Mono, monospace',
        fontWeight: 700,
        color: statusColor.value,
        offsetCenter: [0, '30%'],
        formatter: (val: number) =>
          props.value !== null ? val.toFixed(1) : '--',
      },
      data: [{ value: props.value ?? 0 }],
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
  min-height: 260px;
}

.gauge-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 0.5rem;
}

.gauge-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.gauge-value {
  font-size: 1rem;
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
</style>
