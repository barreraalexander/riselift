<template>
    <section id="NewSessionView">
        <div class="content_ctnr">
            <div class="new_workout_ctnr">
                <div class="session_ctnr" v-show="!new_session_name">
                    <h1>
                        New Workout
                    </h1>
                    <div class="form_group">
                        <label for="session_name">
                            Session Name
                        </label>
                        <input
                            id="session_name"
                            name="session_name"
                            type="text"
                            placeholder="Workout #"
                        >
                    </div>
                </div>
                <div class="data_ctnr">
                    <div class="working_ctnr" v-show="new_session_id">
                        <form action="" id="new_exercise">

                            <div class="form_group">
                                <label>
                                    Name
                                </label>
                                <input
                                    id="exercise_name"
                                    type="text"
                                    placeholder="Monthly Max Out"
                                >
                            </div>

                            <div class="form_group">
                                <label for="">
                                    Weight
                                </label>
                                <input
                                    id="exercise_weight"
                                    type="text"
                                    placeholder="0"
                                    value="0"
                                >
                                <div class="alter_exercise_ctnr">
                                    <button id="add_weight" @click="alter_exercise($event)" data-operand="5">
                                        +5
                                    </button>
                                    <button id="sub_weight" @click="alter_exercise($event)" data-operand="5">
                                        -5
                                    </button>
                                </div>
                            </div>

                            <div class="form_group">
                                <select
                                    name="exercise_unit"
                                    id="exercise_unit"
                                >
                                    <option value="lbs">
                                        lbs
                                    </option>
                                    <option value="kgs">
                                        kgs
                                    </option>

                                </select>
                            </div>


                            <div class="form_group">
                                <label for="">
                                    Reps
                                </label>

                                <input
                                    id="exercise_reps"
                                    type="text"
                                    placeholder="0"
                                    value="0"
                                >
                                <div class="alter_exercise_ctnr">
                                    <button id="add_rep" @click="alter_exercise($event)" data-operand="5">
                                        +5
                                    </button>
                                    <button id="sub_rep" @click="alter_exercise($event)" data-operand="5">
                                        -5
                                    </button>
                                </div>

                            </div>

                            <div class="form_group">
                                <button @click="createExercise($event)" role="submit">Add</button>
                            </div>
                        </form>

                    </div>



                    <div class="completed_ctnr">

                    </div>
                </div>
            </div>

            <div class="start_workout_ctnr">
                <div @click="createWorksession" class="start_button">
                    <p>
                        Start a New Workout
                    </p>
                </div>
            </div>

        </div>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            new_session_id: '',
            new_session_name: '',
            new_session_last_index: 0,
        }
    },
    methods : {
        async createWorksession(){
            let session_name = document.querySelector('#session_name').value


            let new_workout = {
                name: session_name   
            }

            let result = await axios.post('http://localhost:5000/worksessions', new_workout)

            if (result.data){
                this.new_session_id = result.data.id
                this.new_session_name = result.data.name
                let content_ctnr = document.querySelector('.content_ctnr')
                content_ctnr.style.flexFlow = 'column-reverse'
            }




        },
        async createExercise(event){
            event.preventDefault()
            let name = document.querySelector('#exercise_name')
            let rep_count = document.querySelector('#exercise_reps')
            let weight = document.querySelector('#exercise_weight')
            let exercise_unit = document.querySelector('#exercise_unit')

            let new_exercise = {
                name: name.value,
                list_index: this.new_session_last_index,
                rep_count: rep_count.value,
                weight: weight.value,
                weight_type: exercise_unit.value,
                worksession_id: this.new_session_id
            }

            let result = await axios.post('http://localhost:5000/exercises', new_exercise)
            if (result.data){
                this.new_session_last_index += 1
                rep_count.value = 0
            }
 
        },
        alter_exercise(event){
            event.preventDefault()
            
            let weight = document.querySelector('#exercise_weight')
            let weight_int = parseInt(weight.value)

            let rep = document.querySelector('#exercise_reps')
            let rep_int = parseInt(rep.value)

            let operand= parseInt(event.target.dataset.operand)

            if (event.target.id==='add_weight'){
                weight_int += operand
            }

            if (event.target.id==='sub_weight'){
                weight_int -= operand
            }

            if (event.target.id==='add_rep'){
                rep_int += operand
            }

            if (event.target.id==='sub_rep'){
                rep_int -= operand
            }

            weight.value = weight_int
            rep.value = rep_int
        }
    }
}

</script>


<style lang="scss">

#NewSessionView{
    form{
        display: contents;
    }
    .content_ctnr{
        padding: 2em;
        align-items: center;
        display: flex;
        flex-flow: column;
        gap: 2em;


        .start_button{
            display: flex;
            flex-flow: column;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: green;
            color: #fff;
            height: 10em;
            width: 10em;
        }
        .start_button:hover{
            cursor: pointer;
        }
    }
    .working_ctnr{
        display: flex;
        flex-flow: column;
        gap: 2em;
    }
    .form_group{
        display: flex;
        flex-flow: column;
        gap: .25em;
    }

    .completed_ctnr{
        display: flex;
        justify-content: flex-start;
    }
}

</style>