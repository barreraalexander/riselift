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

<script lang="ts">
import { defineComponent, PropType } from "vue";
import ProgramSlideVue from "../pieces/ProgramSlide.vue";
import ButtonLikeVue from '../pieces/ButtonLike.vue';

export default defineComponent({
    name: "AboutProgram",
    data: () => ({
        slide_index : 0
    }),
    methods: {
        alter_program : function(event: Event){
            let slides = document.querySelectorAll('.slide');
            let right_arrow = document.querySelector('#right_arrow') as HTMLElement | null;
            let left_arrow = document.querySelector('#left_arrow') as HTMLElement | null;

            // slides[this.slide_index].style.display = "none"
            
            if (event.target===right_arrow){
                this.slide_index += 1
            } else if (event.target===left_arrow){
                this.slide_index -= 1
            }

            if (this.slide_index>=slides.length || this.slide_index<0){
                this.slide_index = 0
            }
            // slides[this.slide_index].style.display = "block"

        }
    },
    components: {
        ProgramSlideVue,
        ButtonLikeVue
    }
})



</script>

<style lang="scss">
#AboutProgram{
    align-items: center;
    background: $proj_primary;
    display: flex;
    flex-flow: column;
    gap: 1em;
    padding: 2em;
    position: relative;
    h1, h4, p{
        text-align: center;
    } 
    .program_slide_ctnr{
        display: flex;
        align-items: center;
        margin-top: 2em;
        gap: 2em;
    }
    .slide_bg{
        position: absolute;
        width: 100%;
        top: 0;
        left: 0;
        display: none;
    }
    
    #left_arrow,
    #right_arrow{
        cursor: pointer;
        background: #000;
        height: 2em;
        width: 2em;
    }
    
    #right_arrow{
        clip-path: polygon(75% 0%, 100% 50%, 75% 100%, 0% 100%, 25% 50%, 0% 0%);    
    }
    
    #left_arrow{
        clip-path: polygon(100% 0%, 75% 50%, 100% 100%, 25% 100%, 0% 50%, 25% 0%);
    }
}



</style>