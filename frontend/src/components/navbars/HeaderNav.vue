<template>
<section id="HeaderSection">
    <nav>
        <img
            src="../../assets/images/icons/kaiyote1.svg"
            class="logo"
            alt=""
        >
        <div class="nav_ctnr">
            <ul>
                <li>
                    <router-link to="/">Home</router-link>
                </li>
                <li>
                    <router-link to="/register">Sign Up</router-link>
                </li>
            </ul>
        </div>
    </nav>
</section>
</template>


<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'HeaderNav',
})
</script>


<style lang="scss">
#HeaderSection{
    height: 2em;
    background: #fff;
    padding: .5em;
    a{
        color: #000;
    }
    
    nav{
        display: flex;
        align-items: center;
    }

    .logo{
        width: 2em;
        margin-right: auto;
    }
    
    .logo:hover{
        cursor: pointer;
    }
    
    
    .nav_ctnr ul{
        list-style: none;
        display: flex;
        gap: 1em;
    }
    
    .nav_ctnr li:hover{
        cursor: pointer;
    }
}




</style>