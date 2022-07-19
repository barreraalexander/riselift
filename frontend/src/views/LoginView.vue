<template>
    <section id="LoginView">
        <div class="login_panel login_decoration">
        </div>
        <div class="login_panel login_form_ctnr">
            <div class="button_ctnr">
                <button id="login_button" @click="handleChangeForm">
                    Login
                </button>
                <button id="register_button">
                    Register
                </button>
            </div>
            <h1>
                Login
            </h1>
            <form action="">
                <div class="form_group">
                    <label for="">
                        Username
                    </label>
                    <input type="text">
                </div>
                <div class="form_group">
                    <label for="">
                        Password
                    </label>
                    <input type="text">
                </div>
                <div class="form_group">
                    <button role="submit">subimt</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>


export default {
    methods: {
        handleChangeForm(){
            alert('here')
        }
    }
}
</script>


<style lang="scss">
@import '@/assets/scss/views/LoginView.scss';
</style>