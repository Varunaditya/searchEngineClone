<template>
    <div>
      <div class="row">
        <div class="col-md-6 col-md-offset-3 col-sm-12 ">
          <br><br>
            <form class="form-group">
              <label for="searchQuery">Search</label>
              <input type="text"
                     class="form-control"
                     v-model="searchQuery">
            </form>
          <ul class="list-group"
              v-if="items.length">
            <li v-for="item in items"
                class="list-group-item">{{ item }}</li>
          </ul>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "Search",
        data(){
          return {
            searchQuery: '',
            items: []
          };
        },
        mounted(){
          window.hinterXHR = new XMLHttpRequest();
        },
        methods: {
          hinter(event){
            var app = this;
            var minChars = 3;
            if (app.searchQuery.length < minChars) {
              app.items = [];
              return;
            }
            else {
              window.hinterXHR.abort();
              window.hinterXHR.onreadystatechange = function(){
                if(this.readyState == 4 && this.status == 200) {
                  var response = JSON.parse(this.responseText);
                  app.items = response;
                }
              };
              window.hinterXHR.open('GET', '/api/search?name=' + app.searchQuery, true);
              window.hinterXHR.send();
            }
          }
        }
    }
</script>

<style scoped>

</style>
