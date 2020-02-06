import Vue from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import {BootstrapVue} from "bootstrap-vue"

import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {faPlus, faMinus, faChevronLeft, faTimes, faCheck, faHandHoldingUsd, faUser} from '@fortawesome/free-solid-svg-icons'
library.add(faPlus, faMinus, faChevronLeft, faTimes, faCheck, faHandHoldingUsd, faUser)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

Vue.use(BootstrapVue)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
