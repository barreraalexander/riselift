<script setup>
import HeaderVue from './components/navbars/HeaderNav.vue';
import FooterVue from './components/navbars/FooterNav.vue';
</script>
    
<template>
    <section id="AppSection">
        <HeaderVue/>
        <router-view/>
        <FooterVue/>
    </section>
</template>

<style lang="scss">
@import "@/assets/scss/base/base.scss";
@import "@/assets/scss/base/typography.scss";
@import "@/assets/scss/base/classes.scss";
</style>