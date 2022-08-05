
<script setup>
import DashboardProfile from "@/components/pieces/DashboardProfile.vue";
import DashboardAddNew from "@/components/pieces/DashboardAddNew.vue";
import LastWorkSummary from "@/components/pieces/LastWorkSummary.vue";
</script>



<template>
    <section id="DashboardSection">
        <h1>Dashboard</h1>
        <div class="panels_ctnr">
            <div class="desktop_ctnr">
                <DashboardProfile/>
                <DashboardAddNew/>
            </div>
            <LastWorkSummary/>
        </div>
    </section>
</template>


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