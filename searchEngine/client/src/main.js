// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import search from './components/Search.vue'
import insert from './components/Insert.vue'


Vue.config.productionTip = false

Vue.use(VueRouter);

const routes= [
  {'path': '/', component: search},
  {'path': '/insert', component: insert}
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
