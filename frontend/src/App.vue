<script>
import { defineComponent } from 'vue';
import HeaderVue from './components/navbars/HeaderNav.vue';
import FooterVue from './components/navbars/FooterNav.vue';


export default defineComponent({
    name: 'App',
    components: {
        HeaderVue,
        FooterVue
    }
})

</script>
<template>
    <section id="AppSection">
        <HeaderVue/>
        <!-- <router-view/> -->
        <FooterVue/>
    </section>
</template>



<style lang="scss">
@import "@/assets/scss/base/base.scss";
@import "@/assets/scss/base/typography.scss";
@import "@/assets/scss/base/classes.scss";
</style>