<template>
<section id="AppSection">
    <HeaderNav/>
    <router-view/>
    <FooterNav/>
</section>
</template>


<script lang="ts">
import { defineComponent } from 'vue';
import HeaderNav from './components/navbars/HeaderNav.vue';
import FooterNav from './components/navbars/FooterNav.vue'

export default defineComponent({
    name: 'App',
    components: {
        HeaderNav,
        FooterNav
    }
})

</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
