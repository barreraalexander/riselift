<template>
    <section id="AddSession">
        <div class="add_session_ctnr">
            <h2>
                Add Exercise
            </h2>
            <form id="session_form" action="">
                <div class="form_ctnr">
                    
                    <div class="form_group">

                        <label for="name">
                            Name
                        </label>
                        <input type="text" :value="name" @input="$emit('input')">
                    </div>

                    <div class="form_group">
                        <label for="">
                            Session Start
                        </label>
                        <input type="text" v-model="start">
                    </div>

                    <div class="form_group">
                        <label for="">Session End</label>
                        <input type="text" v-model="end">
                    </div>
                    
                    <div class="form_group">
                        <button @click="$emit('submit')">submit</button>
                    </div>

                </div>
            </form>

        </div>

    </section>
</template>

<script>



export default {
    data: () => ({
        valid: true,
        name: "",
        start: "",
        end: "",
    }),
}

</script>