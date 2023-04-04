<template>
    <div id="admin-page">

        <b-modal id="payment" hide-header hide-footer>
            <h2 class="text-center text-muted">User</h2>
            <b-form-select size="lg" class="shadow mb-3" v-model="payment_user"
                           :options="paymentUserOptions"></b-form-select>
            <h2 class="text-center text-muted">Amount</h2>
            <h2 class="text-center text-muted">{{payment_amount+' €'}}</h2>
            <div class="text-center">
                <b-button-group size="md" class="mb-3 d-flex flex-row shadow">
                    <b-button variant="outline-secondary" v-for="number in 10" :key="'number-'+number"
                              @click="payment_amount += number-1">
                        <h3>{{number - 1}}</h3>
                    </b-button>
                    <b-button variant="outline-secondary" @click="payment_amount = payment_amount.slice(0, -1)">
                        <font-awesome-icon :icon="['fas','backspace']"/>
                    </b-button>
                </b-button-group>
            </div>
            <b-button @click="pay" class="shadow" block size="lg" variant="success"
                      :disabled="payment_user == null || parseInt(payment_amount) <= 0 || parseInt(payment_amount) >= 500"><h1>Confirm payment</h1>
            </b-button>
        </b-modal>


            <b-card-body class="d-flex flex-column">
                    <h1 class="logo gradient-text">Cassies</h1>
                    <h5 class="text-muted">Admin Page</h5>
                    <div class="mb-3">
                        <hr>
                    </div>
                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                    @click="addPayment">
                        Add Payment
                    </b-button>

                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                        @click="$router.push('/admin-page/user-management')">
                        Manage Users
                    </b-button>

                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3" 
                        @click="$router.push('/admin-page/item-management')">
                        Manage Items
                    </b-button>

                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                        Other
                    </b-button>
                    <b-button pill size="1g"  block variant="outline-secondary" class="shadow mb-3"
                    @click="$router.push('/')">
                        Back
                    </b-button>

                    <p class="text-muted mt-auto mb-0">Made with ❤ <br> by Robert i312 and upgraded by Anton i303</p>
            </b-card-body>
    </div>
</template>

<script>
import axios from "axios";
    export default {
        

        name: "Admin",
        created() {
            this.getUsers()
        },
        data() {
            return {
                active_users: [],
                inactive_users: [],
                payment_user: null,
                payment_amount: 0,

            }
        },
        computed: {
        paymentUserOptions() {
                let active = []
                this.active_users.forEach((user) => {
                    active.push({
                        value: user,
                        text: user.name + (user.hasOwnProperty('room') ? ' i3' + user.room : '')
                    })
                })
                let inactive = []
                this.inactive_users.forEach((user) => {
                    inactive.push({value: user, text: user.name})
                })
                return [{label: 'Active users', options: active}, {label: 'Inactive users', options: inactive}]
            }
        },
        methods: {
            pay() {
                let transaction = {
                        'user': this.payment_user,
                        'payment': true,
                        'impact': parseInt(this.payment_amount) * 100
                    }
                    axios.post(this.$parent.host + '/transactions/add', transaction).then(() => {
                        this.$parent.CDPmessage({top: {center: 'Payment added!'}}, 10)
                        this.$bvModal.hide('payment')
                    }).catch((error) => {
                        console.log(error)
                        this.$bvModal.hide('payment')
                    })
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
            },
            addPayment() {
                this.payment_user = null
                this.payment_amount = ''
                this.$bvModal.show('payment')
            }
        }
    }
</script>

<style scoped>
    .empty-cart {
        height: 100%;
    }

    .gif {
        flex-grow: 1;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        border-radius: 6px;
    }

    .quantity-selector {
        min-width: 135px;
    }

    .expand {
        height: calc(100vh - 340px);
        overflow: hidden;
    }

    .item-bar {
        overflow-x: scroll;
    }

    .item-container {
        min-width: 250px;
    }

    .item-image {
        height: 100px;
        margin: 1px;
        position: relative;
        z-index: 1;
    }

    .item-image.middle {
        height: 120px;
    }

    .bottle-shadow {
        width: 160px;
        max-width: 100%;
        position: relative;
        bottom: 50px;
        margin-bottom: -50px;
    }

    .item-values {
        float: right;
        margin-left: 10px;
        margin-top: -5px;
        text-align: right;
    }

    .item-volume {
        margin-top: -5px;
    }

    .like-icon {
        position: absolute;
        right: 20px;
    }

    .purple-gradient {
        background: rgb(214, 0, 255);
        background: linear-gradient(90deg, rgba(214, 0, 255, 1) 0%, rgba(255, 218, 0, 1) 100%);
    }
</style>