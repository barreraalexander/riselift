<template>
    <div :id="slide_id" class="slide">
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


<style lang="scss">
@import "@/assets/scss/pieces/ProgramSlide.scss";
</style>