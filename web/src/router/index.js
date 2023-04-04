import Vue from 'vue'
import VueRouter from 'vue-router'
import UserSelection from '../views/UserSelection.vue'
import ItemSelection from "../views/ItemSelection";
import TransactionList from "../views/TransactionList";
import AdminPage from "../views/AdminPage/AdminPage";
import UserManagement from "../views/AdminPage/UserManagement";
import ItemManagement from "../views/AdminPage/ItemManagement";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'user-selection',
        component: UserSelection
    },
    {
        path: '/item-selection',
        name: 'item-selection',
        component: ItemSelection
    },
    {
        path: '/transaction-list',
        name: 'transaction-list',
        component: TransactionList
    },
    {
        path: '/admin-page',
        name: 'admin-page',
        component: AdminPage
    },
    {
        path: '/admin-page/user-management',
        name: 'user-management',
        component: UserManagement
    },
    {
        path: '/admin-page/item-management',
        name: 'item-management',
        component: ItemManagement
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
