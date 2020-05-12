<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <About msg="CS450 JSON Protocol Vue.js Client"/>
    <!-- Fetch Dewpoint Data -->
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Vue Axios Post and Return Response Data</div>
                    <br>
                    <div class="card-body">
                        <form @submit="getDewpointData">
                          <button class="btn btn-success">Fetch Dewpoint Data from SQLite Database</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Display Dewpoint Data -->
    <BarChart v-bind:seriesDews="dewPoints" :seriesYears="years" :isDisabled="isDisabled"/>

    <!-- Wanted to implement conditions and more as promised, but data was not incorporated in backend -->
    <!-- Fetch Weather Conditions Data -->
    <!-- <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <br>
                    <div class="card-body">
                        <form @submit="getConditionsData">
                          <button class="btn btn-success">Fetch Conditions Data from SQLite Database</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div> -->
    <DonutChart />
  </div>
</template>

<script>
import About from './components/About.vue'
import BarChart from './components/SeriesBarChart.vue'
import DonutChart from './components/DonutChart.vue'

export default {
  name: 'App',
  components: {
    About,
    BarChart,
    DonutChart
  },
  data() {
    return {
      output: '',
      //initialize arrays to send to charts
      years: [],
      dewPoints: [],
      isDisabled: true
      //condCounts: []
    };
  },
  methods: {
    //GET & send 'years' arrays with corresponding avg dew points for that year
    getDewpointData(e) {
        e.preventDefault()
        let currentObj = this
        let config = {
          headers: {
            "Content-Type":"application/json"
          }
        }
        currentObj.isDisabled = false
        this.axios.post('http://localhost:8080/', {
          //server expecting
          "method": "select",
          "where": {"y":"10"}
        }, config)
        .then(function (response) {
            currentObj.output = response.data
            //init variables to parse and send years/ dewPoints data to charts
            let dewData = currentObj.output.rows
            let date,year
            let dew,avgDewD,dewTotal = 0,dewCount = 0,eCount = 0
            let dewLen = dewData.length
            dewData.forEach (e => {
              //e[0] = dewPoint
              //e[1] = datetime
              date = e[1]
              dew = e[0]
              //convert year strings to integers for charts
              year = parseInt(date.slice(0,4))
              //if year != last year index, divide dewTotal / count, then reset count & dewTotal
              if (currentObj.years.includes(year) == false) {
                //init dewTotal and dewCount on first year
                if (currentObj.years.length < 1) {
                  dewTotal = dew
                  dewCount = 1
                  currentObj.years.push(year)
                  eCount += 1
                  return
                }
                //catch last forEach iteration to push last year's dewPoint

                currentObj.years.push(year)
                avgDewD = dewTotal / dewCount;
                //push dewPoint for last year
                currentObj.dewPoints.push(avgDewD)
                dewTotal = 0
                dewCount = 0
              //else if year at current index == year of last index, year is the same, add to dewTotal
              }else if (currentObj.years.includes(year)) {
                dewTotal += dew
                dewCount += 1
                if (eCount == dewLen-1) {
                  console.log("Last element of dewData here")
                  avgDewD = dewTotal / dewCount;
                  //push dewPoint for last year
                  currentObj.dewPoints.push(avgDewD)
                }
              }
              eCount += 1
            })
        })
        .catch(function (error) {
            currentObj.output = error
        });
    },
    // getConditionsData(e) {
    //     e.preventDefault();
    //     let condsObj = this;
    //     let config = {
    //       headers: {
    //         "Content-Type":"application/json"
    //       }
    //     }
    //     this.axios.post('http://localhost:8080/', {
    //       //server expecting
    //       "method": "select"
    //     }, config)
    //     .then(function (response) {
    //         condsObj.output = response.data
    //         //extract _conds from data
    //         let resData = condsObj.output.rows
    //         let hazeCount=0,smokeCount=0,clearCount=0,pcCount=0,fogCount=0,shFogCount=0,rainCount=0
    //         //count each individual conds
    //         resData.forEach(e => {
    //           condition = e[3]
    //
    //           switch (condition) {
    //             case 'Haze':
    //               hazeCount += 1
    //               break
    //             case 'Smoke':
    //               smokeCount += 1
    //               break
    //             case 'Clear':
    //               clearCount += 1
    //               break
    //             case 'Partly Cloudy':
    //               pcCount += 1
    //               break
    //             case 'Fog':
    //               fogCount += 1
    //               break
    //             case 'Shallow Fog':
    //               shFogCount += 1
    //               break
    //             case 'Rain':
    //               rainCount += 1
    //           }
    //         })
    //         //send conds counts to donut to display
    //     })
    //     .catch(function (error) {
    //         condsObj.output = error;
    //     });
    // }
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
