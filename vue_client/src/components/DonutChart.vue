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
        labels: ["Haze","Smoke","Clear", "Partly Cloudy", "Fog", "Shallow Fog","Rain"],
        title: {
              text: "Weather Conditions in New Delhi"
        }
      },
      //series represents counts of data points
      series: [7268, 4023, 2242, 5093, 4911, 3063, 1254]
    }
  }
}
</script>
