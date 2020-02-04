<template>
    <div id="app">
        <router-view v-if="data != null"/>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        created() {
            this.preventContextMenu()
            this.getData()
        },
        data() {
            return {
                data: null,
                selected_user: null
            }
        },
        methods: {
            preventContextMenu() {
                document.addEventListener("contextmenu", function (e) {
                    e.preventDefault();
                }, false)
            },
            getData() {
                const path = 'http://100.124.99.212:5000/data'
                axios.get(path).then((res) => {
                    this.data = res.data
                })
                .catch((error) => {
                    console.error(error)
                })
            }
        }
    }

</script>

<style>
    @import "./assets/sass/fonts.scss";

    #app {
        font-family: "Helvetica Neue", Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
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
</style>
