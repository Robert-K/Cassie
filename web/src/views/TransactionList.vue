<template>
    <div id="transaction-list">
        <div v-if="transactions != null" style="height: 100vh; overflow: hidden">
            <b-card no-body class="shadow mx-3 my-4">
                <b-card-body class="p-0">
                    <div class="p-3 text-left">
                        <b-button pill @click="$router.push('/')" class="shadow" variant="outline-secondary">
                            Back
                        </b-button>
                    </div>
                    <b-modal id="undo-modal" title="You are about to permanently undo this transaction.">
                        <b-img class="shadow" fluid :src="require('@/assets/images/gifs/invisible.gif')"/>
                        <template v-slot:modal-footer>
                            <b-button block size="lg" variant="danger" @click="undoTransaction(undo_date)"
                                      class="shadow">
                                Undo transaction
                            </b-button>
                        </template>
                    </b-modal>
                    <b-table no-border-collapse sticky-header="84vh" striped sort-by="date" sort-desc
                             class="text-left mb-0"
                             :items="transactions" :fields="fields">
                        <template v-slot:head(payment)>
                            <font-awesome-icon :icon="['fas','hand-holding-usd']"/>
                        </template>
                        <template v-slot:cell(payment)="data">
                            <font-awesome-icon v-if="data.value === true" :icon="['fas','hand-holding-usd']"/>
                        </template>
                        <template v-slot:head(guest)>
                            <font-awesome-icon :icon="['fas','user']"/>
                        </template>
                        <template v-slot:cell(guest)="data">
                            <font-awesome-icon v-if="data.value === true" :icon="['fas','user']"/>
                        </template>
                        <template v-slot:cell(items)="data">
                            <div v-for="item in data.value" :key="item.barcode">{{item.quantity}}x {{item.name}}
                                {{item.variant}}
                                {{formatVolume(item.volume)}}
                            </div>
                        </template>
                        <template v-slot:cell(balance)="data">
                            <div :style="{color: balanceColor(data.item.user.balance + data.item.impact)}">
                                {{formatPrice(data.item.user.balance + data.item.impact)}}
                            </div>
                        </template>
                        <template v-slot:head(undo)>
                            <div/>
                        </template>
                        <template v-slot:cell(undo)="data">
                            <b-button :id="'button-undo-transaction' + data.index" variant="danger" class="shadow"
                                      v-if="isLessThenHalfAnHourAgo(data.item.date)"
                                      @click="showUndoModal(data.item.date)">Undo
                            </b-button>
                        </template>
                    </b-table>
                </b-card-body>
            </b-card>
        </div>
    </div>
</template>

<script>
    import axios from "axios"

    const interpolate = require('color-interpolate')

    const moment = require('moment');

    export default {
        name: "TransactionList",
        created() {
            this.getTransactions()
        },
        data() {
            return {
                transactions: null,
                fields: [
                    {key: 'user.name', label: 'User', sortable: true},
                    {key: 'user.id', label: 'ID', sortable: true},
                    {key: 'payment', sortable: true},
                    {key: 'guest', sortable: true},
                    {key: 'items', sortable: true},
                    {key: 'impact', formatter: 'formatPrice', sortable: true},
                    {key: 'balance'},
                    {key: 'date', sortable: true},
                    {key: 'undo'}
                ],
                undo_date: null
            }
        },
        methods: {
            formatPrice(value) {
                return (value / 100).toFixed(2) + '€'
            },
            formatVolume(value) {
                return value + 'l'
            },
            balanceColor(balance) {
                let map = interpolate(['green', 'orange', 'red'])
                return map(Math.max((-balance / 100) / 100, 0))
            },
            getTransactions() {
                axios.get(this.$parent.host + '/transactions').then((res) => {
                    this.transactions = res.data
                }).catch((error) => {
                    console.error(error)
                })
            },
            showUndoModal(date) {
                this.undo_date = date
                this.$bvModal.show('undo-modal')
            },
            undoTransaction(date) {
                this.$bvModal.hide('undo-modal')
                axios.post(this.$parent.host + '/transactions/undo', {date: date}).then(() => {
                    this.$parent.CDPmessage({top: 'Transaction undone!'}, 10)
                    this.getTransactions()
                }).catch((error) => {
                    console.log(error)
                    this.getTransactions()
                })
            },
            isLessThenHalfAnHourAgo(date) {
                return moment().subtract(60, 'minutes') < moment(date, 'DD/MM/YYYY, HH:mm:ss')
            }
        }
    }
</script>

<style scoped>

</style>