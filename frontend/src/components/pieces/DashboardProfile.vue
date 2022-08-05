<template>
    <div class="dashboard_profile">
        <p>hi</p>
        <p>{{this.user['email']}}</p>
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
            let result = await axios.get('http://localhost:5000/users/6')
            if (result.data){
                return result.data
            }
        },
        async getWorksessions(){
            let result = await axios.get('http://localhost:5000/worksessions')
            if (result.data){
                return result.data
            }
        }
    },
    mounted : async function(){
        let user = await this.getUser()
        this.user = user

        let user_exercises = await this.getWorksessions()
        this.user_exercises = user_exercises
    }
}

</script>


<style lang="scss">

.dashboard_profile{
    background: black;
    color: white;
    width: 80%;
    height: 20vh;
    border-radius: 20px;
}

</style>