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
              <br>
              <button class="btn-success btn"
                      @click.prevent="getQuery">Search</button>
            </form>
          <span v-if="items.length"
                v-for="item in items">
            <div class="card">
              <div class="card-header">
                {{ item.title }}
              </div>
              <div class="card-body justify-content">
                <p class="card-text">{{ item.content }}</p>
              </div>
            </div>
            <br>
          </span>
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
              window.hinterXHR.open('GET', '/api/search?title=' + app.searchQuery, true);
              window.hinterXHR.send();
            }
          },
          getQuery(){
              this.hinter();
          }
        }
    }
</script>

<style scoped>

</style>
