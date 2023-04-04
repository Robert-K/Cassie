<template>
    <div id="user-selection">
        <b-row class="py-4 px-3 full-height m-0" v-if="active_users != null">
            <b-modal id="enter-pin" hide-header hide-footer>
                <h2 class="text-center text-muted">Pin</h2>
                <div class="text-center">
                    <b-button-group size="md" class="mb-3 d-flex flex-row shadow">
                        <b-button variant="outline-secondary" v-for="number in 10" :key="'number-'+number"
                                  @click="pin_code += number-1">
                            <h3>{{number - 1}}</h3>
                        </b-button>
                        <b-button variant="outline-secondary" @click="pin_code = pin_code.slice(0, -1)">
                            <font-awesome-icon :icon="['fas','backspace']"/>
                        </b-button>
                    </b-button-group>
                </div>
                <h2 class="text-center text-muted">{{pin_code}}</h2>
                <b-button @click="admin" class="shadow" block size="lg" variant="success"
                          :disabled="pin_code !== '9312'"><h1>Enter</h1>
                </b-button>
            </b-modal>
            <b-col cols="3" class="d-flex flex-column px-0">
                <b-card no-body class="shadow" style="flex-grow: 1">
                    <b-card-body class="d-flex flex-column">
                        <h1 class="logo gradient-text">Cassie</h1>
                        <h5 class="text-muted">Hydration Systems</h5>
                        <div class="mb-3">
                            <hr>
                        </div>
                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                                  @click="$router.push('/transaction-list')">
                            Transactions
                        </b-button>

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                                  @click="key = (key+1) % sorting_keys.length">
                            Sort by: {{sorting_keys[key]}}
                        </b-button>

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                                  @click="showEnterPin">
                            Admin
                        </b-button>

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                                  @click="screensaver">
                            Screensaver
                        </b-button>

                        <p class="text-muted mt-auto mb-0">Made with ❤ <br> by Robert i312</p>
                    </b-card-body>
                </b-card>
            </b-col>
            <b-col class="d-flex flex-column">
                <b-row>
                    <b-col v-for="user in active_users" :key="'active-' + user.id" cols="4"
                           class="mb-3 pl-3 pr-0 text-muted">
                        <b-card no-body class="shadow" @click="selectUser(user)">
                            <b-card-body class="p-2">
                                <h1 class="room-number"><b>{{user.room}}</b></h1>
                                <div class="user-foreground text-left pl-2">
                                    <h2>{{getUserByID(user.id).name}}</h2>
                                    <h3 :style="{color: balanceColor(getUserByID(user.id).balance)}">
                                        {{formatPrice(getUserByID(user.id).balance)}}</h3>
                                </div>
                            </b-card-body>
                        </b-card>
                    </b-col>
                </b-row>
                <b-modal id="more-users" hide-header hide-footer body-class="pb-0">
                    <b-card v-for="user in inactive_users" :key="'inactive-' + user" class="shadow mb-3 text-muted"
                            @click="selectUser(getUserByID(user))">
                        <b-row>
                            <b-col>
                                <h2>{{getUserByID(user).name}}</h2>
                            </b-col>
                            <b-col><h2 :style="{color: balanceColor(getUserByID(user).balance), float: 'right'}">
                                {{formatPrice(getUserByID(user).balance)}}</h2>
                            </b-col>
                        </b-row>
                    </b-card>
                </b-modal>
                <b-row style="flex-grow: 1">
                    <b-col class="pr-0 text-muted" style="height: 100%">
                        <b-card no-body class="shadow" style="height: 100%" @click="$bvModal.show('more-users')">
                            <b-card-body class="p-2 d-flex flex-column">
                                <h2 class="my-auto">More users</h2>
                            </b-card-body>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
    </div>
</template>

<script>
    import axios from "axios";

    const interpolate = require('color-interpolate')

    export default {
        name: 'user_selection',
        created() {
            this.getUsers()
            this.$parent.CDPclock()
        },
        data() {
            return {
                all_users: [],
                active_users: [],
                inactive_users: [],
                sorting_keys: ['Room', 'Balance'],
                key: 0,
                payment_user: null,
                payment_amount: 30,
                pin_code: ''
            }
        },
        computed: {
            userOptions() {
                let active = []
                this.active_users.forEach((user) => {
                    active.push({
                        value: this.getUserByID(user.id),
                        text: this.getUserByID(user.id).name + ' i3' + user.room
                    })
                })
                let inactive = []
                this.inactive_users.forEach((user) => {
                    inactive.push({value: this.getUserByID(user), text: this.getUserByID(user).name})
                })
                return [{label: 'Active users', options: active}, {label: 'Inactive users', options: inactive}]
            }
        },
        methods: {
            getUserByID(id) {
                let user = this.all_users.find((user) => user.id === id)
                return user
            },
            selectUser(user) {
                this.$parent.selected_user = user
                this.$parent.CDPmessage({
                    top: {center: user.name},
                    bottom: {center: (user.balance / 100).toFixed(2)}}, 2)
                this.$router.push('item-selection')
            },
            formatPrice(value) {
                return (value / 100).toFixed(2) + '€'
            },
            formatPayment(value) {
                return Math.max(value, 1)
            },
            balanceColor(balance) {
                let map = interpolate(['green', 'orange', 'red'])
                return map(Math.max((-balance / 100) / 30, 0))
            },
            getUsers() {
                axios.get(this.$parent.host + '/users').then((res) => {
                    this.all_users = res.data.users
                    this.active_users = res.data.active
                    this.all_users = this.all_users.sort(function (a, b) {
                        if (a.name < b.name) {
                            return -1;
                        }
                        if (a.name > b.name) {
                            return 1;
                        }
                        return 0;
                    });
                    this.all_users.forEach ((user) => {
                        this.inactive_users.push(user.id)
                    })
                    this.active_users.forEach ((user) => {
                        this.inactive_users = this.inactive_users.filter((id) => id !== user.id)
                    })
                }).catch((error) => {
                    console.error(error)
                })
            },
            showEnterPin() {
                this.payment_user = null
                this.payment_amount = 30
                this.pin_code = ''
                this.$bvModal.show('enter-pin')
            },
            admin() {
                this.pin_code = ''
                this.$router.push('/admin-page')
                /**
                    et transaction = {
                        'user': this.payment_user,
                        'payment': true,
                        'impact': this.payment_amount * 100
                    }
                    axios.post(this.$parent.host + '/transactions/add', transaction).then(() => {
                        this.$parent.CDPmessage({top: {center: 'Payment added!'}}, 10)
                        this.$bvModal.hide('payment')
                    }).catch((error) => {
                        console.log(error)
                        this.$bvModal.hide('payment')
                    })
                */
            },
            screensaver() {
                axios.post(this.$parent.host + '/screensaver').catch((error) => {
                    console.log(error)
                })
            }
        }
    }
</script>

<style scoped>
    .full-height {
        height: 100vh;
        width: 100vw;
        overflow: hidden;
    }

    .logo {
        font-size: 62px;
        margin-bottom: -6px;
    }

    .gradient-text {
        background: -webkit-linear-gradient(45deg, #2537AF, #70E5CB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .room-number {
        position: absolute;
        font-size: 80pt;
        right: 10px;
        top: -15px;
        z-index: 0;
        color: #f0f0f0;
    }

    .user-foreground {
        position: relative;
        z-index: 1;
    }
</style>