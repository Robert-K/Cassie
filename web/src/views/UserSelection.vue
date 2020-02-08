<template>
    <div id="user-selection">
        <b-row class="py-4 px-3 full-height m-0" v-if="active_users != null">
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

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Make payment
                        </b-button>

                        <p class="text-muted mt-auto mb-0">Made with ❤ <br> by Robert i312</p>
                    </b-card-body>
                </b-card>
            </b-col>
            <b-col class="d-flex flex-column">
                <b-row>
                    <b-col v-for="user in sortedActiveUsers" :key="user.id" cols="4"
                           class="mb-3 pl-3 pr-0 text-muted">
                        <b-card no-body class="shadow" @click="selectUser(user)">
                            <b-card-body class="p-2">
                                <h1 class="room-number"><b>{{user.room}}</b></h1>
                                <div class="user-foreground text-left pl-2">
                                    <h2>{{user.name}}</h2>
                                    <h3 :style="{color: balanceColor(user.balance)}">
                                        {{formatPrice(user.balance)}}</h3>
                                </div>
                            </b-card-body>
                        </b-card>
                    </b-col>
                </b-row>
                <b-row style="flex-grow: 1">
                    <b-col class="pr-0 text-muted" style="height: 100%">
                        <b-card no-body class="shadow" style="height: 100%">
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
        name: 'user-selection',
        created() {
            this.getUsers()
        },
        data() {
            return {
                active_users: [],
                inactive_users: [],
                sorting_keys: ['Room', 'Balance'],
                key: 0
            }
        },
        computed: {
            sortedActiveUsers() {
                return this.active_users.sort((a, b) => {
                    if (this.key === 0)
                        return a.room - b.room
                    else
                        return a.balance - b.balance
                })
            },
        },
        methods: {
            selectUser(user) {
                this.$parent.selected_user = user
                this.$router.push('item-selection')
            },
            formatPrice(value) {
                return (value / 100).toFixed(2) + '€'
            },
            balanceColor(balance) {
                let map = interpolate(['green', 'orange', 'red'])
                return map(Math.max((-balance / 100) / 100, 0))
            },
            getUsers() {
                axios.get(this.$parent.host + '/users').then((res) => {
                    res.data.users.forEach((user) => {
                        if (user.id in res.data.active_users) {
                            this.active_users.push(user)
                        } else {
                            this.inactive_users.push(user)
                        }
                    })

                }).catch((error) => {
                    console.error(error)
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