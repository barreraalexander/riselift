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
    },
    methods: {
        async generateAuthorizedHeader(){
            let local_user = window.localStorage.getItem("current_user");
            console.log(local_user)
            if (local_user != null) {
                let auth_token = `Bearer ${local_user}`
                let request_config = {
                    headers: {
                        Authorization: auth_token
                    }
                };
                return request_config
            } else {
                return null
            }
        }
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
