<template>
    <section id="LoginView">
        <div class="login_panel login_decoration">
        </div>
        <div class="login_panel login_form_ctnr">
            <div class="button_ctnr">
                <button id="login_button" @click="handleChangeForm">
                    Login
                </button>
                <button id="register_button" @click="handleChangeForm">
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
                    <input type="text" v-model="email">
                </div>
                <div class="form_group">
                    <label for="">
                        Password
                    </label>
                    <input type="text" v-model="password">
                </div>
                <div class="form_group">
                    <button @click="handleSubmit($event)" role="submit">submit</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script lang="ts">
import axios from 'axios';

export default {
    data (){
        return {
            submit_type: 'regiser',
            email: '',
            password: ''
        }
    },
    methods: {
        handleChangeForm(){
            alert('here')
        },
        async handleSubmit(e){
            e.preventDefault()
            // console.log(this.email)
            // console.log(this.password)

            var bodyFormData = new FormData()

            // let form = document.querySelector('#login_form')
            // console.log(form)

            bodyFormData.append(
                'username', this.email
            )

            bodyFormData.append(
                'password', this.password
            )

            // console.log(bodyFormData)
            let result = await axios.post('http://localhost:5000/login', bodyFormData)
            // console.log(result)
            // console.log(result.data.access_token)
         
            let request_config = {
                headers: {
                    Authorization: `Bearer ${result.data.access_token}`

                }
            }
        
            console.log(request_config)


            let current_user = await axios.get('http://localhost:5000/users/current', request_config)
            console.log(current_user)


            // let current_user = localStorage.getItem("current_user");
            // console.log(current_user)


            // alert('submitted')
        }
    },
}
</script>


<style lang="scss">
@import '@/assets/scss/views/LoginView.scss';
</style>