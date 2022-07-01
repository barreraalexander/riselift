<script setup> 
import axios from 'axios';
import { ref } from "vue";

import session_item from '../pieces/session_item.vue';
import AddSession from '../modals/AddSession.vue'
import UpdateSession from '../modals/UpdateSession.vue'

let add_session_data = AddSession.data()
let update_session_data = UpdateSession.data()

let exercise_list = ref([])

async function populateList(){
    let result = await axios.get('http://localhost:5000/worksessions')
        if (result.data){
            exercise_list.value = result.data
        }
}

</script>


<template>
<section id="UserDashboard" v-show="true">
    <div class="sessions_list_ctnr">
        <UpdateSession @submit="updateExercise($event)" @input="WriteInput($event)"/>
        <AddSession @submit="submitExercise($event)" @input="WriteInput($event)"/>
        <h2>
            Sessions List
        </h2>
        <div class="sessions_list">
            <ul>
                <session_item
                    v-for="exercise in exercise_list"
                    :key="exercise.id"
                    :id="exercise.id"
                    :name="exercise.name"
                    @click="handleClick($event, exercise.id)"
                />
            </ul>
        </div>
    </div>
</section>
</template>

<script>

export default {
    data () {
        return {
            valid: true,
            exercises: [],
            text_exer: 1,

        }
    },

    
    methods : {
        async getExercises(){
            let result = await axios.get('http://localhost:5000/worksessions')
            if (result.data){
                return result.data
            }
        },
        async submitExercise(event){
            if (event){
                event.preventDefault();
                let result = await axios.post('http://localhost:5000/worksessions', {
                    name: this.add_session_data.name
                })
                console.log(result)
                this.populateList()

            }
        },
        async deleteExercise(event, id){
            let result = await axios.delete(`http://localhost:5000/worksessions/${id}`)
            this.populateList()
        },
        async updateExercise(event, id){
            let result = await axios.put(`http://localhost:5000/worksessions/${id}`, {
                name: this.update_session_data.name
            })
            this.populateList()
        },
        WriteInput(event){
            if (event){
                let elem = event.target.value

                if (event.target.id=="updateSession_input"){
                    this.update_session_data.name = elem
                    return
                }
                this.add_session_data.name = elem
            }
        },
        handleClick(event, id){
            if (event.target.id=="update_button"){
                this.updateExercise(event, id)
                return
            }
            if (event.target.id=="remove_button"){
                this.deleteExercise(event, id)
                return

            }
            let form = document.querySelector('#session_form')
            form.reset()

        }

    },

    mounted: function(){
        this.populateList()
    }
}
</script>


<style scoped>
.sessions_list ul{
    display: flex;
    flex-flow: column;
    gap: 2em;
    list-style: none;
}

.sessions_list button{
    background:red;
    color: #fff;
}

</style>