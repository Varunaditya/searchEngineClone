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
              <div class="card"
                   v-if="showResult">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item"
                      v-for="item in items"
                      style="cursor: pointer"
                      @click="expandResult(item)">{{ item.title }}</li>
                </ul>
              </div>
              <span v-if="noResultMsg">
                <br>
                <p class="font-weight-bold text-muted text-center">
                  No Result
                </p>
              </span>
              <br>
              <button class="btn-success btn"
                      @click.prevent=""
                      style="display: none;">Search</button>
            </form>
          <span v-if="title">
            <div class="card">
              <div class="card-header">
                {{ title }}
              </div>
              <div class="card-body justify-content">
                <p class="card-text text-justify">{{ content }}</p>
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
            items: [],
            title: '',
            content: '',
            showResult: true,
            noResultMsg: false
          };
        },
        mounted(){
          window.hinterXHR = new XMLHttpRequest();
        },
        watch: {
          searchQuery: function () {
            this.noResultMsg = false;
            this.showResult = true;
            this.hinter();
          }
        },
        methods: {
          hinter(){
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
                  if(app.items.length == 0){
                    app.noResultMsg = true;
                  }
                }
              };
              window.hinterXHR.open('GET', '/api/search?title=' + app.searchQuery, true);
              window.hinterXHR.send();
            }
          },
          expandResult(result){
            this.showResult = false;
            this.title = result.title;
            this.content = result.content;
          }
        }
    }
</script>

<style scoped>

</style>
