<template>
  <div class="card timeseries-card">
    <div class="ts-header">
      <span class="ts-label">{{ label }}</span>
      <span class="ts-current mono" :style="{ color }">
        {{ currentValue !== null ? currentValue.toFixed(2) : '--' }} {{ unit }}
      </span>
    </div>
    <apexchart
      type="area"
      height="200"
      :options="chartOptions"
      :series="series"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const props = defineProps<{
  sensorType: string
  label: string
  unit: string
  color: string
  currentValue: number | null
  normalMin: number
  normalMax: number
}>()

const MAX_POINTS = 60

const dataPoints = ref<{ x: number; y: number }[]>([])

watch(
  () => props.currentValue,
  (newVal) => {
    if (newVal !== null) {
      dataPoints.value.push({ x: Date.now(), y: newVal })
      if (dataPoints.value.length > MAX_POINTS) {
        dataPoints.value = dataPoints.value.slice(-MAX_POINTS)
      }
    }
  }
)

const series = computed(() => [
  {
    name: props.label,
    data: dataPoints.value,
  },
])

const chartOptions = computed(() => ({
  chart: {
    id: `ts-${props.sensorType}`,
    background: 'transparent',
    toolbar: { show: false },
    zoom: { enabled: false },
    animations: {
      enabled: true,
      easing: 'linear',
      dynamicAnimation: { speed: 1000 },
    },
  },
  theme: { mode: 'dark' as const },
  colors: [props.color],
  stroke: {
    curve: 'smooth' as const,
    width: 2,
  },
  fill: {
    type: 'gradient',
    gradient: {
      shadeIntensity: 1,
      opacityFrom: 0.4,
      opacityTo: 0.05,
      stops: [0, 100],
    },
  },
  xaxis: {
    type: 'datetime' as const,
    labels: {
      style: { colors: '#64748b', fontSize: '10px' },
      datetimeFormatter: {
        hour: 'HH:mm',
        minute: 'HH:mm:ss',
      },
    },
    axisBorder: { show: false },
  },
  yaxis: {
    labels: {
      style: { colors: '#64748b', fontSize: '10px' },
      formatter: (val: number) => val.toFixed(1),
    },
  },
  grid: {
    borderColor: '#1e293b',
    strokeDashArray: 4,
  },
  tooltip: {
    theme: 'dark',
    x: { format: 'HH:mm:ss' },
    y: {
      formatter: (val: number) => `${val.toFixed(2)} ${props.unit}`,
    },
  },
  annotations: {
    yaxis: [
      {
        y: props.normalMin,
        borderColor: '#f59e0b',
        strokeDashArray: 4,
        label: {
          text: `Min: ${props.normalMin}`,
          style: { color: '#f59e0b', background: 'transparent', fontSize: '9px' },
          position: 'left' as const,
        },
      },
      {
        y: props.normalMax,
        borderColor: '#f59e0b',
        strokeDashArray: 4,
        label: {
          text: `Max: ${props.normalMax}`,
          style: { color: '#f59e0b', background: 'transparent', fontSize: '9px' },
          position: 'left' as const,
        },
      },
    ],
  },
}))
</script>

<style scoped>
.timeseries-card {
  padding: 1rem;
}

.ts-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.ts-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.ts-current {
  font-size: 0.9rem;
  font-weight: 700;
}
</style>
