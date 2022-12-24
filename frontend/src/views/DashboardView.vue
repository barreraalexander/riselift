<template>

<section id="DashboardSection">
    <h1>Dashboard</h1>

    <div class="panels_ctnr">
        <div class="desktop_ctnr">

            <DashboardProfile v-if="user" :user="user"/>
            <DashboardAddNew/>
        </div>
        <!-- <LastWorkSummary/> -->
    </div>
</section>

</template>

<script lang="ts">
import DashboardProfile from "../components/pieces/DashboardProfile.vue";
import DashboardAddNew from "../components/pieces/DashboardAddNew.vue";
// import LastWorkSummary from "../components/pieces/LastWorkSummary.vue";
import AppVue from "../App.vue";

let app_methods = AppVue.methods

import { defineComponent, ref } from "vue";
import User from '../types/User'
// import Exercise from "../types/Exercise";
import axios from 'axios'

export default defineComponent({
    name: "DashboardView",
    setup() {
        // const user = ref<User>();
        const user = ref<User>();
        // const exercises = ref<Exercise[]>()
        return { user };
    },
    methods: {
        async loadUser(get_request_config=false) {
            // let current_user = await axios.get
            let request_config =  await app_methods?.generateAuthorizedHeader()
            // console.log(request_config)
            if (request_config != null){
                let current_user = await axios.get('http://localhost:5000/users/current', request_config)
                if (current_user.data) {
                    this.user = current_user.data;
                    // console.log(current_user.data)
                    // return current_user.data
                    if (get_request_config){
                        return request_config
                    }

            }


                    return current_user.data
                } else {
                    // redirect to home or login or something because the token has expired
                }
            }
        }
    },
    mounted: function () {
        this.loadUser();
    },
    components: {
        DashboardProfile,
        DashboardAddNew
    }
}
    
)

</script>