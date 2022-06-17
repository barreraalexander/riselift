<template>
    <section id="UpdateSession">
        <div class="update_session_ctnr">
            <h2>
                Update Session
            </h2>
            <form id="update_session_form" action="">
                <div class="form_ctnr">
                    
                    <div class="form_group">
                        <label for="">
                            Name
                        </label>
                        <input id="updateSession_input" type="text" :value="name" @input="$emit('input')" >
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


<style lang="scss">
@import "@/assets/scss/modals/UpdateSession.scss"
</style>