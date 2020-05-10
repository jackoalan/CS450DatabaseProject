module.exports = {
  configureWebpack: {
    devServer: {
      port: 3000,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
        "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
     },
      proxy: {
        '/': {
          target: 'http://localhost:8080'
        }
      }
    }
  }
};
