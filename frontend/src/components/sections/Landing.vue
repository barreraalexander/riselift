<script setup>
import axios from 'axios'

import Login from '../modals/Login.vue';
import Register from '../modals/Register.vue';

import StorySection from './StorySection.vue';
import AboutProgram from './AboutProgram.vue';
import AboutMe from './AboutMe.vue';

import ButtonLike from '../pieces/button_like.vue';



</script>

<template>
    <section id="Landing">
        <div class="landing_ctnr">
            <div class="landing1 landingdiv">
                <img src="../../assets/images/exercise1.jpg" alt="">

            </div>
            <div class="landing2 landingdiv">
                <h1>
                    This is a bold statement about the product, and the key to a good sell is some good words.
                </h1>
                <p>
                    Velit eu laboris aliqua adipisicing eu ex anim excepteur est id velit non tempor. Dolore cillum voluptate dolor consequat Lorem tempor excepteur. Anim nisi ullamco labore nulla dolor tempor ipsum sunt sunt quis magna occaecat. Laboris voluptate non consectetur pariatur fugiat reprehenderit culpa culpa.
                </p>
                <ButtonLike message="demo"/>
            </div>
        </div>
        <StorySection />
        <img
            class="wave_transition"
            src="../../assets/images/icons/orange_wave2.svg"
            alt=""
        >
        <AboutProgram />
        <img
            class="wave_transition2"
            src="../../assets/images/icons/orange_wave2.svg"
            alt=""
        >
        <AboutMe />
        <Register v-show="false"/>
        <Login v-show="false"/>
    </section>
</template>

<style>
#Landing{
    /* height: 100vh; */
    background: #f4f4f4;
}
.landing_ctnr{
    display: flex;
    /* flex-flow: row wrap; */
    flex-flow: column;
    height: 100%;
}
.landing_ctnr h1{
    text-align: center;
}

.landingdiv{

    /* flex: 1; */
}

.landing1{
    overflow: hidden;
    max-height: 50vh;
    background: var(--proj_primary);

}
.landing1 img{
    width: 100%;
    
}


.landing2{
    flex: 1;
    display: flex;
    flex-flow: column;
    gap: 2em;
    padding: 2em;   
}

.landing2 h1{
    text-align: left;
}

.landing2 button{
    width: 10em;
}

.wave_transition{
    position: relative;
    bottom: -.25em;
}

.wave_transition2{
    transform: rotate(180deg);
}



@media only screen and (min-width: 767px){
    .landing_ctnr{
        flex-flow: row;
    }
}

</style>