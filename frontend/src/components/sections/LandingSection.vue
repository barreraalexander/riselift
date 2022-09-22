<template>

<section id="Landing">
    <div class="landing_ctnr">
        <div class="landing1 landingdiv">
            <img
                src="../../assets/images/exercise1.jpg"
                alt=""
            >
        </div>
        <div class="landing2 landingdiv">
            <h1>
                This is a bold statement about the product, and the key to a good sell is some good words.
            </h1>
            <p>
                Velit eu laboris aliqua adipisicing eu ex anim excepteur est id velit non tempor. Dolore cillum voluptate dolor consequat Lorem tempor excepteur. Anim nisi ullamco labore nulla dolor tempor ipsum sunt sunt quis magna occaecat. Laboris voluptate non consectetur pariatur fugiat reprehenderit culpa culpa.
            </p>
            <ButtonLikeVue message="demo"/>
        </div>
    </div>
</section>
</template>

<script lang="ts">
import ButtonLikeVue from '../pieces/ButtonLike.vue';
import { defineComponent, ref } from 'vue';

export default defineComponent({
    name: 'LandingSection',
    components: {
        ButtonLikeVue
    }
})

</script>



<style lang="scss">
#Landing{
    background: #f4f4f4;
    .landing_ctnr{
        display: flex;
        flex-flow: column;
        height: 100%;
        h1{
            text-align: center;
        }
    }    
    .landing1{
        overflow: hidden;
        background: var(--proj_primary);
        img{
            width: 100%;
        }
    
    }
    .landing2{
        flex: 1;
        display: flex;
        flex-flow: column;
        gap: 2em;
        padding: 2em;
        h1{
            text-align: left;
        }
    }
    
    .wave_transition{
        position: relative;
        bottom: -.25em;
    }
    
    .wave_transition2{
        transform: rotate(180deg);
    }
}



@media only screen and (min-width: 767px){
    .landing_ctnr{
        flex-flow: row;
    }
}


</style>