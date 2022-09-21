<template>
    <section id="LandingView">
      <LandingSectionVue/>
      <StorySectionVue/>
      <img
          id="wavetop"
          src="@/assets/images/icons/orange_wave1.svg"
          alt=""
      >
      <AboutProgramVue/>
      <img
          id="wavebottom"
          src="@/assets/images/icons/orange_wave1.svg"
          alt=""
      >
      <AboutMeVue/>
    </section>
</template>
  
<script lang="ts">
import LandingSectionVue from '../components/sections/LandingSection.vue';
import StorySectionVue from '../components/sections/StorySection.vue';
import AboutProgramVue from '../components/sections/AboutProgram.vue';
import AboutMeVue from '../components/sections/AboutMe.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'LandingView',
    components: {
        LandingSectionVue,
        StorySectionVue,
        AboutProgramVue,
        AboutMeVue
    }
})


</script>