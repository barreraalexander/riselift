<template>
    <section id="NewSessionView">
        <div class="content_ctnr">
            <div class="new_workout_ctnr">
                <h1>
                    New Workout
                </h1>
                <p>
                    Name
                </p>
                <input
                    type="text"
                    placeholder="Monthly Max Out"
                >
                
                <div class="data_ctnr">
                    <div class="working_ctnr">
                        <div class="form_group">
                            
                            <label for="">
                                Weight
                            </label>
                            <input type="text" placeholder="0">



                            <input
                                type="radio"
                                name="weight_type"
                                value="lbs"
                            >
                            <label for="pounds">
                                Pounds
                            </label>
                            
                            <input
                                type="radio"
                                name="weight_type"
                                value="kgs"
                            >
                            <label for="kilograms">
                                Kilograms
                            </label>


                        </div>
                        <div class="form_group">
                            <label for="">
                                Reps
                            </label>
                            <input type="text" placeholder="0">
                        </div>
                        

                    </div>
                    <div class="completed_ctnr">

                    </div>
                </div>
            </div>

            <div class="start_workout_ctnr">
                <div @click="createWorksession($event)" class="start_button">
                    <p>GO!</p>
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
            new_session: '',
            new_session_name: '',
        }
    },
    methods : {
        async createWorksession(event){
            let new_workout = {
                name: 'testname'   
            }

            let result = await axios.post('http://localhost:5000/worksessions', new_workout)

            if (result.data){
                console.log(result.data)
            }
            
            event.target.style.display = 'none'


        }
    }
}

</script>


<style lang="scss">

#NewSessionView{
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
    }
}

</style>