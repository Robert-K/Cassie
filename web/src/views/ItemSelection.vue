<template>
    <div class="item-selection">
        <b-row class="item-bar flex-nowrap m-0 px-2">
            <b-card no-body v-for="item in data.items" :key="item.barcode" class="item-container mx-2 my-4 shadow"
                    @click="addItem(item)">
                <b-card-body>
                    <b-img :src="require('@/assets/images/items/'+item.image)" class="item-image"/>
                    <b-img :src="require('@/assets/images/items/'+item.image)" class="item-image middle"/>
                    <b-img :src="require('@/assets/images/items/'+item.image)" class="item-image"/>
                    <b-img :src="require('@/assets/images/bottle_shadow.png')" class="bottle-shadow"/>
                    <b-card-text class="text-left">
                        <div class="item-values">
                            <h3><b>{{formatPrice(item.price)}}</b></h3>
                            <h6 class="item-volume text-muted">{{formatVolume(item.volume)}}</h6>
                        </div>
                        <h6>{{item.name}}</h6>
                        <h5><b>{{item.variant}}</b></h5>
                    </b-card-text>
                </b-card-body>
            </b-card>
        </b-row>
        <b-row class="m-0 flex-nowrap">
            <b-col cols="7">
                <b-card class="shadow text-left expand">
                    <b-table :items="selected_items" :fields="fields" v-if="selected_items.length > 0">
                        <template v-slot:cell(product)="data">
                            {{data.item.name}} <b>{{data.item.variant}}</b> {{formatVolume(data.item.volume)}}
                        </template>
                        <template v-slot:cell(quantity)="data">
                            <b-input-group class="shadow quantity-selector">
                                <b-input-group-prepend>
                                    <b-btn variant="outline-danger"
                                           @click="removeItem(data.item)">
                                        <font-awesome-icon :icon="['fas','minus']"/>
                                    </b-btn>
                                </b-input-group-prepend>
                                <b-form-input type="number" v-model="data.item.quantity" class="text-center"
                                              :formatter="formatQuantity"
                                              style="width: 10px;" size="lg"/>
                                <b-input-group-append>
                                    <b-btn variant="outline-success"
                                           @click="addItem(data.item)">
                                        <font-awesome-icon :icon="['fas','plus']"/>
                                    </b-btn>
                                </b-input-group-append>
                            </b-input-group>
                        </template>
                    </b-table>
                    <div v-else class="d-flex flex-column empty-cart">
                        <h5>Dein Einkaufswagen ist leer.</h5>
                        <p>Wähle Produkte aus,
                            indem du sie oben antippst oder ihren Barcode scannst.</p>
                        <b-img class="gif"
                               :src="'@assets/images/gifs/' + this.gifs[Math.floor(Math.random()*(this.gifs.length-1))]"/>
                    </div>
                </b-card>
            </b-col>
            <b-col class="pl-0">
                <b-card no-body class="shadow expand">
                    <b-card-body class="d-flex flex-column">
                        <h1>Gesamt: {{formatPrice(getTotal())}}</h1>
                        <h4 class="text-muted my-auto">Mahamomandalanta<br>Guthaben: -4,00€</h4>
                        <b-form-checkbox size="lg" v-model="guest">Als Gast markieren
                        </b-form-checkbox>
                        <b-button size="lg" variant="success" class="mt-auto shadow"
                                  :disabled="selected_items.length === 0"><h1>Bestätigen</h1></b-button>
                        <b-button size="lg" variant="secondary" class="mt-3 shadow"><h1>Abbrechen</h1></b-button>
                    </b-card-body>
                </b-card>
            </b-col>
        </b-row>
    </div>
</template>

<script>
    import json from '@/data.json'

    export default {
        created() {
            document.addEventListener("contextmenu", function (e) {
                e.preventDefault();
            }, false)
        },
        data() {
            return {
                data: json,
                selected_items: [],
                fields: [
                    {key: 'product', label: 'Produkt'},
                    {key: 'price', label: 'Stückpreis', formatter: 'formatPrice'},
                    {key: 'quantity', label: 'Anzahl', thClass: 'text-center', tdClass: 'text-center'}
                ],
                gifs: ['crash.gif', 'dog.gif', 'drunk.gif', 'faceplant.gif', 'house.gif',
                    'knight.gif', 'loop.gif', 'mario.gif', 'moonwalk.gif', 'panda.gif', 'race.gif',
                    'run.gif', 'skate.gif', 'snow.gif', 'space.gif', 'titanic.gif', 'truck.gif'],
                guest: false
            }
        },
        methods: {
            addItem(item_to_add) {
                let matching_item = this.selected_items.filter(item => {
                    return item.barcode === item_to_add.barcode
                })[0]
                if (matching_item) {
                    this.$set(matching_item, 'quantity', Number(matching_item.quantity) + 1)
                } else {
                    item_to_add = {...item_to_add}
                    item_to_add.quantity = 1
                    this.selected_items.push(item_to_add)
                }
            },
            removeItem(item_to_remove) {
                let matching_item = this.selected_items.filter(item => {
                    return item.barcode === item_to_remove.barcode
                })[0]
                if (matching_item) {
                    if (matching_item.quantity > 1) {
                        this.$set(matching_item, 'quantity', Number(matching_item.quantity) - 1)
                    } else {
                        let index = this.selected_items.indexOf(matching_item);
                        if (index !== -1) this.selected_items.splice(index, 1);
                    }
                }
            },
            formatQuantity(value) {
                return Math.max(value, 1).toString()
            },
            formatPrice(value) {
                return (value / 100).toFixed(2) + '€'
            },
            formatVolume(value) {
                return value + 'l'
            },
            getTotal() {
                let total = 0
                this.selected_items.forEach(item => {
                    total += Number(item.price) * Number(item.quantity)
                })
                return total
            }
        }
    }
</script>

<style>
    .empty-cart {
        height: 100%;
    }

    .gif {
        border-radius: 4px;
    }

    .quantity-selector {
        min-width: 135px;
    }

    .expand {
        height: calc(100vh - 340px);
        overflow: hidden;
    }

    ::-webkit-scrollbar {
        display: none;
    }

    * {
        cursor: none;
        scrollbar-width: none;
        -webkit-user-select: none; /* Chrome all / Safari all */
        -moz-user-select: none; /* Firefox all */
        -ms-user-select: none; /* IE 10+ */
        user-select: none; /* Likely future */
        touch-action: manipulation;
    }

    input[type=number]::-webkit-outer-spin-button,
    input[type=number]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }

    input[type=number] {
        -moz-appearance: textfield;
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

    .purple-gradient {
        background: rgb(214, 0, 255);
        background: linear-gradient(90deg, rgba(214, 0, 255, 1) 0%, rgba(255, 218, 0, 1) 100%);
    }
</style>