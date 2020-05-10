<template>
   <div>
     <apexcharts width="50%" type="line" :options="options" :series="series"></apexcharts>
   </div>
</template>

<script>
 import VueApexCharts from 'vue-apexcharts'

 export default {
   name: 'LineChart',
   components: {
     apexcharts: VueApexCharts,
   },
   data: function() {
     return {
       options: {
         chart: {
           id: 'vuechart-example'
         },
         xaxis: {
           categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
         }
       },
       series: [{
         name: 'series-2',
         data: [30, 40, 45, 50, 49, 60, 70, 91]
       }]
     }
   }
 }
</script>
