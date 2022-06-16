<template>
    <div :id="slide_id" class="slide">
        <!-- <img
            class="slide_bg"
            src="../../assets/images/exercise1.jpg"
            alt=""
        > -->
        <div class="slide_number">
            <p>
                {{slide_content[slide_id]["slide_num"]}}
            </p>
        </div>
        <h4>
            {{slide_content[slide_id]["heading"]}}
        </h4>
        <p>
            I've worked in all kinds of environments, with all kinds of equipment, from bands, to weights, to no equipment at all.
        </p>                
    </div>
</template>

<script>

export default{
    data: () => ({
        slide_content: {
            "slide1" : {
                'slide_num' : '1',
                'heading' : 'Work with the Equipment you already Have',
                'blurb' : "I've worked in all kinds of environments, with all kinds of equipment, from bands, to weights, to no equipment at all."
            },
            "slide2" : {
                'slide_num' : '2',
                'heading' : "We'll Build the Workout Routine",
                'blurb' : "Depending on how much time you have to spare a week, we'll put together a schedule so that we can workout."
            },
            "slide3" : {
                'slide_num' : '3',
                'heading' : 'Get Healthy from Home',
                'blurb' : "I've worked in all kinds of environments, with all kinds of equipment, from bands, to weights, to no equipment at all."
            },
            "slide4" : {
                'slide_num' : '4',
                'heading' : 'Tracking Workouts, Sometihng Accountability',
                'blurb' : "I've worked in all kinds of environments, with all kinds of equipment, from bands, to weights, to no equipment at all."
            },

        }
    }),

    props: {
        slide_id: { required: true, type: String }
    }
}


</script>


<style scoped>

.slide{
    height: 18em;
    width: 12em;
    border: 4px solid #000;
    background: var(--proj_gray);
    border-radius: 10px;
    padding: 1em;
    display: flex;
    flex-flow: column;
    gap: 1em;
    position: relative;
    transition: 1s;
}


.slide_number{
    border-radius: 50%;
    color: #fff;
    background: #000;
    height: 3em;
    width: 3em;
    position: absolute;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    top: -1.5em;
    left: 12.5em;
}


h1, h4, p{
    text-align: center;
}



</style>