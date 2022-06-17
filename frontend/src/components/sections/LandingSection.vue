<script setup>
import ButtonLikeVue from '../pieces/ButtonLike.vue';
</script>

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

<style lang="scss">
@import "@/assets/scss/sections/Landing.scss"
</style>