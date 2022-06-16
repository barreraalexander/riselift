<script setup>
import slide from '../pieces/slide.vue';
import button_like from '../pieces/button_like.vue';
</script>

<template>
    <section id="AboutProgram">
        <h1>
            How the Program Works
        </h1>
        <div class="program_slide_ctnr">
            <div id="left_arrow" @click="alter_program($event)"></div>
            
            <slide slide_id="slide1" />
            <slide slide_id="slide2" v-show="false"/>
            <slide slide_id="slide3" v-show="false"/>
            <slide slide_id="slide4" v-show="false"/>

            <div id="right_arrow" @click="alter_program($event)"></div>
        </div>
        <button_like message="demo"/>
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

<style scoped>
#AboutProgram{
    background: var(--proj_primary);
    padding: 2em;
    display: flex;
    flex-flow: column;
    align-items: center;
    gap: 1em;
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

h1, h4, p{
    text-align: center;
}




</style>