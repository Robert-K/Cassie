<template>
    <div id="transaction-list">
        <b-table :items="data.transactions" :fields="fields"/>
    </div>
</template>

<script>
    export default {
        name: "TransactionList",
        data() {
            return {
                data: this.$parent.data,
                fields: [
                    {key: 'user.name', label: 'User'},
                    {key: 'guest'},
                    {key: 'items'},
                    {key: 'amount', formatter: 'formatPrice'},
                    {key: 'date'}
                ]
            }
        },
        methods: {
            formatPrice(value) {
                return (value / 100).toFixed(2) + '€'
            }
        }
    }
</script>

<style scoped>

</style>