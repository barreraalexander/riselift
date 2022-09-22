<template>
    <div class="add_new_workout">
        <button @click="handleClick">new workout</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "@vue/runtime-core"


export default defineComponent({
    methods: {
        handleClick(){
            window.location.href = 'http://localhost:8080/new_session'
        }
    }
}
)
</script>

<style lang="scss">
.add_new_workout{
    padding: 2em;
    // background: green;
}

</style>

