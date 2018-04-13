import Vue from 'vue'
import Router from 'vue-router'
import Vuetify from 'vuetify'
Vue.use(Vuetify)
const routerOptions = [
  { path: '/', component: 'WebPlayer' },
  { path: '/about', component: 'About' },
  { path: '*', component: 'NotFound' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
