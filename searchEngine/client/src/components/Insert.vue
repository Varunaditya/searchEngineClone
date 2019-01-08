<template>
    <div>
      <section>
        <div class="container">
          <div class="col-md-6 col-md-offset-3 col-sm-12">
            <form class="form-group">
              <label for="title">Title</label>
              <input type="text"
                     class="form-control"
                     v-model="title">
              <br>
              <label for="content">Content</label>
              <textarea class="form-control"
                        v-model="content"></textarea>
              <br>
              <button class="btn btn-success"
                      @click.prevent="insertQuery">Submit</button>
            </form>
          </div>
        </div>
      </section>
    </div>
</template>

<script>
    export default {
        name: "Insert",
        data() {
          return {
            title: '',
            content: ''
          };
        },
      methods: {
          insertQuery(){
            let queryTitle = this.title;
            let queryContent = this.content;
            fetch('api/insert', {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({title: queryTitle, 'content': queryContent})
            });
            this.title = '';
            this.content = '';
          }
      }
    }
</script>

<style scoped>

</style>
