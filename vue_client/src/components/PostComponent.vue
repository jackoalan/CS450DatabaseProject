<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Vue Axios Post</div>

                    <div class="card-body">
                        <form @submit="formSubmit">
                          <button class="btn btn-success">Submit</button>
                        </form>
                        <pre>
                          {{output}}
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        },
        data() {
          return {
            output: ''
          };
        },
        methods: {
            formSubmit(e) {
                e.preventDefault();
                let currentObj = this;
                let config = {
                  headers: {
                    "Content-Type":"application/json"
                  }
                }
                this.axios.post('http://localhost:8080/', {
                  //server expecting
                  "method": "select",
                  "where": {"y":"10"}
                }, config)
                .then(function (response) {
                    currentObj.output = response.data;
                })
                .catch(function (error) {
                    currentObj.output = error;
                });
            }
        }
    }
</script>
