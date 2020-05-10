<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="CS450 JSON Protocol Vue.js Client"/>
    <PostComponent/>
    <DonutChart />
    <BarChart />

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import PostComponent from './components/PostComponent.vue'
import BarChart from './components/SeriesBarChart.vue'
import DonutChart from './components/DonutChart.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    PostComponent,
    BarChart,
    DonutChart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
