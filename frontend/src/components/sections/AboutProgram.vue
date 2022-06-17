<script setup>
import ButtonLikeVue from '../pieces/ButtonLike.vue';
import ProgramSlideVue from '../pieces/ProgramSlide.vue';
</script>

<template>
    <section id="AboutProgram">
        <h1>
            How the Program Works
        </h1>
        <div class="program_slide_ctnr">
            <div id="left_arrow" @click="alter_program($event)"></div>
            <ProgramSlideVue slide_id="slide1" />
            <ProgramSlideVue slide_id="slide2" v-show="false"/>
            <ProgramSlideVue slide_id="slide3" v-show="false"/>
            <ProgramSlideVue slide_id="slide4" v-show="false"/>
            <div id="right_arrow" @click="alter_program($event)"></div>
        </div>
        <ButtonLikeVue message="demo"/>
    </section>
</template>



<script>



export default {
    data: () => ({
        slide_index : 0
    }),
    methods: {
        alter_program : function(event){
            let slides = document.querySelectorAll('.slide')
            let right_arrow = document.querySelector('#right_arrow');
            let left_arrow = document.querySelector('#left_arrow');

            slides[this.slide_index].style.display = "none"
            
            if (event.target===right_arrow){
                this.slide_index += 1
            } else if (event.target===left_arrow){
                this.slide_index -= 1
            }

            if (this.slide_index>=slides.length || this.slide_index<0){
                this.slide_index = 0
            }
            slides[this.slide_index].style.display = "block"

        }
    }
}

</script>

<style lang="scss">
@import "@/assets/scss/sections/AboutProgram.scss"

</style>