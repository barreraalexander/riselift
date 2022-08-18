<template>
    <div class="dashboard_profile">
        <p>hi</p>
        <p>{{this.user['email']}}</p>
        <ul class="exercises_ctnr">
            <div
                class="exercise_ctnr"
                v-for="exercise in user_exercises"
                :key="exercise.id"
                :id="exercise.id"
                :name="exercise.name"
            >
                <p @click="showExerciseModal">
                    {{exercise.name}}
                </p>
            </div>
        </ul>
        <div class="exercise_modal">
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            user: {},
            user_exercises: [],

        }
    },
    methods : {
        async getUser(){
            let result = await axios.get('http://localhost:5000/users/1')
            if (result.data){
                return result.data
            }
        },
        async getWorksessions(){
            let result = await axios.get('http://localhost:5000/worksessions')
            if (result.data){
                return result.data
            }
        },
        showExerciseModal(){
            // should it be a modal or an exercise
        }
    },
    mounted : async function(){
        let user = await this.getUser()
        this.user = user

        let user_exercises = await this.getWorksessions()
        this.user_exercises = user_exercises

        console.log(this.user_exercises)
    }
}

</script>


<style lang="scss">

.dashboard_profile{
    background: black;
    color: white;
    width: 80%;
    // height: 20vh;
    border-radius: 20px;
    .exercises_ctnr{
        background: red;
        margin-top: 2em;

    }
}


</style>