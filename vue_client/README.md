# Vue Client developed by Nico Del Moral

This vue.js client works with node.js and is configured to hit the HTTP endpoints at localhost:8080.  Axios, a promise-based HTTP client was used to make simple CRUD operations to interact with data through the Python backend.  ApexCharts, a JavaScript graphic charts library, was incorporated to display a graphical interface for the data received through the JSON protocol.  Multiple components were loaded in intially but only the About.vue, SeriesBarChat.vue, and DonutChart.vue components were used in the main App.vue /src file.

## Project setup/ install dependencies
```
npm install
```

### Compiles and minifies for production.  
#### Build configured to localhost:8080
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
