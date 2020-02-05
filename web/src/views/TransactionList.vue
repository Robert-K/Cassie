<template>
    <div id="transaction-list">
        <b-card no-body class="shadow mx-3 my-4">
            <b-card-body class="p-0">
                <div class="p-3 text-left">
                    <b-button pill @click="$router.push('/')" class="shadow" variant="outline-secondary">
                        Back
                    </b-button>
                </div>
                <b-table no-border-collapse sticky-header="91vh" striped sort-by="date" sort-desc class="text-left"
                         :items="data.transactions" :fields="fields">
                    <template v-slot:cell(guest)="data">
                        <font-awesome-icon v-if="data.value === true" :icon="['fas','check']"/>
                        <font-awesome-icon v-else :icon="['fas','times']"/>
                    </template>
                    <template v-slot:cell(items)="data">
                        <div v-for="item in data.value" :key="item.barcode">{{item.quantity}}x {{item.name}}
                            {{item.variant}}
                            {{formatVolume(item.volume)}}
                        </div>
                    </template>
                    <template v-slot:cell(balance)="data">
                        <div :style="{color: balanceColor(data.item.user.balance - data.item.amount)}">
                            {{formatPrice(data.item.user.balance - data.item.amount)}}
                        </div>
                    </template>
                </b-table>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
    const interpolate = require('color-interpolate')

    export default {
        name: "TransactionList",
        data() {
            return {
                data: this.$parent.data,
                fields: [
                    {key: 'user.name', label: 'User', sortable: true},
                    {key: 'guest', sortable: true},
                    {key: 'items', sortable: true},
                    {key: 'amount', formatter: 'formatPrice', sortable: true},
                    {key: 'balance'},
                    {key: 'date', sortable: true}
                ]
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
                return map(Math.max((-balance / 100) / 120, 0))
            }
        }
    }
</script>

<style scoped>

</style>