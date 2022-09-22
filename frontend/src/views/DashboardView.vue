<template>

<section id="DashboardSection">
    <h1>Dashboard</h1>
    <div class="panels_ctnr">
        <div class="desktop_ctnr">
            <DashboardProfile :user="user"/>
            <DashboardAddNew/>
        </div>
        <!-- <LastWorkSummary/> -->
    </div>
</section>

</template>

<script lang="ts">
import DashboardProfile from "../components/pieces/DashboardProfile.vue";
// import DashboardAddNew from "../components/pieces/DashboardAddNew.vue";
// import LastWorkSummary from "../components/pieces/LastWorkSummary.vue";

import { defineComponent, ref } from "vue";
import User from '../types/User'
import axios from 'axios'

export default defineComponent({
    name: "DashboardView",
    setup() {
        const user = ref<User>();
        return { user };
    },
    methods: {
        async loadUser() {
            let local_user = window.localStorage.getItem("current_user");
            if (local_user != null) {
                let request_config = {
                    headers: {
                        // Authorization: `Bearer ${local_user}`
                        Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNSwiZXhwIjoxNjYzODE5NzYwfQ.N7o3kIrBmA0qn5k91CnSbdBSD7oZXHJYzBO3PB8PJKA`
                    }
                };
                let current_user = await axios.get<User>("http://localhost:5000/users/current", request_config)
                if (current_user) {
                    this.user = current_user.data;
                }
            } else {
                console.log('here')
            }
        }
    },
    mounted: function () {
        this.loadUser();
    },
    components: {
        DashboardProfile
    }
}
    
)

</script>