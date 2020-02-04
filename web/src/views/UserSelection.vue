<template>
    <div id="user-selection">
        <b-row class="py-4 px-3 full-height m-0">
            <b-col cols="3" class="d-flex flex-column pr-0">
                <b-card no-body class="shadow" style="flex-grow: 1">
                    <b-card-body class="d-flex flex-column">
                        <h1 class="logo gradient-text">Cassie</h1>
                        <div class="mb-3">
                            <hr>
                        </div>
                        <b-button size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Transactions
                        </b-button>

                        <b-button size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Make payment
                        </b-button>

                        <b-button size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Statistics
                        </b-button>

                        <b-button size="lg" block variant="outline-secondary" class="shadow mb-3">
                            Hidden feature
                        </b-button>

                        <p class="text-muted mt-auto mb-0">Made with ❤ <br> by Robert i312</p>
                    </b-card-body>
                </b-card>
            </b-col>
            <b-col>
                <b-row>
                    <b-col v-for="user in data.users" :key="user.id" cols="4" class="mb-3 pl-3 pr-0 text-muted">
                        <b-card no-body class="shadow">
                            <b-card-body class="p-2">
                                <h2>{{user.name}}</h2>
                                <h3 v-bind:style="{color: user.balance < 0 ? 'red' : 'green'}">
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
    export default {
        name: 'user-selection',
        data() {
            return {
                data: this.$parent.data
            }
        },
        methods: {
            hashCode(str) { // java String#hashCode
                let hash = 0;
                for (let i = 0; i < str.length; i++) {
                    hash = str.charCodeAt(i) + ((hash << 5) - hash);
                }
                return hash;
            },
            intToRGB(i) {
                let c = (i & 0x00FFFFFF)
                    .toString(16)
                    .toUpperCase();

                return "00000".substring(0, 6 - c.length) + c;
            },
            formatQuantity(value) {
                return Math.max(value, 1).toString()
            },
            formatPrice(value) {
                return (value / 100).toFixed(2) + '€'
            },
            formatVolume(value) {
                return value + 'l'
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
    }

    .gradient-text {
        background: -webkit-linear-gradient(45deg, #2537AF, #70E5CB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>