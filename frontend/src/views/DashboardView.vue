<template>
    <section id="DashboardSection">
        <h1>Dashboard</h1>
        <div class="panels_ctnr">
            <div class="desktop_ctnr">
                <!-- <DashboardProfile/> -->
                <DashboardAddNew/>
            </div>
            <LastWorkSummary/>
        </div>
    </section>
</template>

<script lang="ts">
// import DashboardProfile from "../components/pieces/DashboardProfile.vue";
import DashboardAddNew from "../components/pieces/DashboardAddNew.vue";
import LastWorkSummary from "../components/pieces/LastWorkSummary.vue";


import { defineComponent} from 'vue';
// import  User from '../types/User'
// import axios from 'axios'

export default defineComponent({
    name: 'DashboardView',
    // setup(){
    //     const user = ref<User>()
    //     return { user }
    // },
    // methods: {
    //     async loadUser(){
    //         let local_user = window.localStorage.get('current_user')
    //         if (local_user != null){
    //             console.log(local_user)
    
    //             let result = await axios.post(`http://localhost:5000/users/${local_user}`)
    //             if (result.data){
    //                 console.log(result.data)
    //             }

    //         }

    //     }
    // },
    // mounted: function(){
    //     // this.loadUser()
    //     // console.log(this.user)

    // },
    components: {
        DashboardAddNew,
        LastWorkSummary,
        
    }

})


</script>


<style lang="scss">

#DashboardSection{
    .panels_ctnr{
        display: flex;
        flex-flow: column;
        align-items: center;
        padding: 2em 0;

        // background: red;
        // height: 100vh;

    }

    .desktop_ctnr{
        display: contents;
    }
}

@media only screen and (min-width: $desktop_bp){
    .panels_ctnr{
        flex-flow: row;
    }
    .desktop_ctnr{
        display: flex;
    }

}


</style>