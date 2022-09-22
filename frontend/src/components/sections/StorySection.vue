<template>

<section id="story_section">
    <h2>
        Fitness is Complicated
    </h2>
    <p>
        And you don't have to learn about it on your own
    </p>
    <div class="media_ctnr">
    </div>
</section>

</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'StorySection'
})

</script>

<style lang="scss">
#story_section {
    padding: 1em;
    display: flex;
    flex-flow: column;
    align-items: center;
    gap: 2em;
    background: #fff;
    h2,p{
      text-align: center;
    }
    .media_ctnr{
      background: #000;
      width: 80%;
      height: 10em;
    
    }
}
  
</style>
  