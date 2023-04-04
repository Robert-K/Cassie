<template>
    <div id="user-management">
            <b-card-body class="d-flex flex-column">
                    <h1 class="logo gradient-text">Cassies</h1>
                    <h5 class="text-muted">User Management</h5>
                    <div class="mb-3">
                        <hr>
                    </div>
                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3"
                    @click="addUser">
                        Add User
                    </b-button>

                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                        Manage Active Users
                    </b-button>

                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3" >
                        Show Users
                    </b-button>

                    <b-button pill size="lg" block variant="outline-secondary" class="shadow mb-3">
                        Other
                    </b-button>
                    <b-button pill size="1g"  block variant="outline-secondary" class="shadow mb-3"
                    @click="$router.push('/admin-page')">
                        Back
                    </b-button>

                    <p class="text-muted mt-auto mb-0">Made with ❤ <br> by Robert i312 and upgraded by Anton i303</p>
            </b-card-body>
    </div>
</template>

<script>
import axios from "axios"
    export default {
        name: "Admin",
        created() {
            this.Admin()
        },
        data() {
            return {
                
            }
        },
        methods: {
            addUser() {
                let user = {
                    "name": "Name",
                    "balance": 0,
                    "favorites": []
                    }
                    axios.post(this.$parent.host + '/users/add', user).then(() => {
                        this.$parent.CDPmessage({top: {center: 'User added!'}}, 10)
                        this.$bvModal.hide('add-user')
                    }).catch((error) => {
                        console.log(error)
                    })
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