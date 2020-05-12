<template>
  <div>
    <br>
    <p> Once the Data is fetched from the server/dB, press the button below to load data into the charts </p>
    <button @click="updateChart" :disabled="isDisabled">Load Fetched Data into Charts</button>
    <br>
    <apexcharts width="80%" type="bar" :options="options" :series="series"></apexcharts>
    <apexcharts width="80%" type="line" :options="options" :series="series"></apexcharts>

  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'BarChart',
  components: {
    apexcharts: VueApexCharts,
  },
  props: {
    seriesYears: Array,
    seriesDews: Array,
    isDisabled: Boolean
  },
  data: function() {
    return {
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
        },
        yaxis: {
          decimalsInFloat: 0,
          min: 12000
        },
        dataLabels: {
          enabled:false
        },
        title: {
          text: "Average DewPoint Time Series"
        }
      },
      series: [{
        name: 'Average DewPoint',
        data: []
      }]
    }
  },
  methods: {
    updateChart() {
      this.options.xaxis = { categories:this.seriesYears }
      this.series = [{ data:this.seriesDews }]
    }
  }
}
</script>
