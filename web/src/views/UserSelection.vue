<template>
    <div id="user-selection">
        <b-row class="py-4 px-3 full-height m-0">
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

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Make payment
                        </b-button>

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Statistics
                        </b-button>

                        <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Hidden feature
                        </b-button>

                        <p class="text-muted mt-auto mb-0">Made with ❤ <br> by Robert i312</p>
                    </b-card-body>
                </b-card>
            </b-col>
            <b-col>
                <b-row>
                    <b-col v-for="user in data.users" :key="user.id" cols="4" class="mb-3 pl-3 pr-0 text-muted">
                        <b-card no-body class="shadow" @click="selectUser(user)">
                            <b-card-body class="p-2">
                                <h2>{{user.name}}</h2>
                                <h3 :style="{color: balanceColor(user.balance)}">
                                    {{formatPrice(user.balance)}}</h3>
                            </b-card-body>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
    </div>
</template>

<script>
    const interpolate = require('color-interpolate')

    export default {
        name: 'user-selection',
        data() {
            return {
                data: this.$parent.data
            }
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
                return map(Math.max((-balance / 100) / 120, 0))
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
</style>