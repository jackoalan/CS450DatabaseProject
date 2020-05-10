<template>
  <div>
    <apexcharts width="80%" type="donut" :options="options" :series="series"></apexcharts>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'DonutChart',
  components: {
    apexcharts: VueApexCharts,
  },
  data: function() {
    return {
      options: {
        chart: {
          id: 'vuechart-donut'
        },
        plotOptions: {
              pie: {
                donut: {
                  labels: {
                    show: true,
                    total: {
                      showAlways: true,
                      show: true
                    }
                  }
                }
              }
            },
        labels: ["Smoke", "Haze", "Clear", "Partly Cloudy", "Rain"],
        title: {
              text: "Weather Status in New Delhi"
        }
      },
      series: [30, 40, 45, 50, 49]
    }
  }
}
</script>
