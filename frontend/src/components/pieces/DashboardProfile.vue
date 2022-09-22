<template>
    <div class="dashboard_profile">
        <p>
            hi {{user.email}}
        </p>


<!-- <ul class="exercises_ctnr">
    <div
        class="exercise_ctnr"
        @click="showExerciseModal"
        v-for="exercise in user_exercises"
        :key="exercise.id"
        :id="exercise.id"
        :name="exercise.name"
    >
        <p>
            {{exercise.name}}
        </p>
    </div>
</ul> -->
        <div class="exercise_modal">
            

        </div>

</div>


</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import User from '../../types/User'

export default defineComponent({
    name: "DashboardProfile",
    props: {
        user: {
            required: true,
            type: Object as PropType<User>
        }
    },

})

</script>