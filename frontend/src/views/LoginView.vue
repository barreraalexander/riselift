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
            <h1 id="action_type_h1">
                Register
            </h1>
            <form action="">
                <div class="form_group" v-show="show_name_input">
                    <label for="name">
                        Name
                    </label>
                    <input type="text" name="name" v-model="name">
                </div>
                <div class="form_group">
                    <label for="email">
                        Email
                    </label>
                    <input type="text" name="email" v-model="email">
                </div>
                <div class="form_group">
                    <label for="password">
                        Password
                    </label>
                    <input type="text" name="password" v-model="password">
                </div>
                <div class="form_group">
                    <button @click="handleSubmit($event)" role="submit">
                        submit
                    </button>
                </div>
            </form>
        </div>
    </section>
</template>

<script lang="ts">

import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent ({
    name: "LoginView",
    data (){
        return {
            submit_type: 'register',
            email: '',
            password: '',
            name: '',
            show_name_input: true
        }
    },
    methods: {
        handleChangeForm(e: Event){
            let change_button = e.target as HTMLElement

            let action_type_h1 = document.querySelector('#action_type_h1') as HTMLElement

            if (change_button.id == 'register_button'){
                this.submit_type = 'register'
                action_type_h1.innerText = 'Register'
            }
            if (change_button.id == 'login_button'){
                this.submit_type = 'login'
                action_type_h1.innerText = 'Login'
            }
        },

        async attemptLogin(){

            var bodyFormData = new FormData()
            bodyFormData.append(
                'username', this.email
            )

            bodyFormData.append(
                'password', this.password
            )

            let result = await axios.post('http://localhost:5000/login', bodyFormData)
            // console.log(result.data)
            let request_config = {
                headers: {
                    Authorization: `Bearer ${result.data.access_token}`

                }
            }

            let current_user = await axios.get('http://localhost:5000/users/current', request_config)
        
            if (current_user.data){
                window.location.href = 'http://localhost:8080/dashboard'
                window.localStorage.setItem('current_user', result.data.access_token)
                
            }
        },
        async attemptRegister(){
            let new_user = {
               name: "Claude",
               email: this.email,
               password: this.password
            }

            let result = await axios.post('http://localhost:5000/users', new_user)
            
            if (result.data){
                console.log(result.data)
            }

        },
        async handleSubmit(e: Event){
            e.preventDefault()
            if (this.submit_type == 'login'){
                this.attemptLogin()
            }
            
            if (this.submit_type == 'register'){
                this.attemptRegister()
            }



        }
    },
})

</script>

<style lang="scss">
#LoginView{
    display: flex;
    height: 100vh;
    // background: $proj_gray;
    background: $proj_lprimary;
    .login_panel{
        flex: 1;
    }
    .login_decoration{
        background: url('@/assets/images/exercise1.jpg');
        background-position: center;
        background-size: cover;        
    }
    .login_form_ctnr{
        align-items: center;
        display: flex;
        flex-flow: column;
        gap: 1em;
        padding-top: 2em;
        h1{
            color: #000;
        }
    }
    .button_ctnr{
        display: flex;
        button{
            width: 8em;
        }
        #login_button{
            border-radius: 10px 0px 0px 10px;
        }
        #register_button{
            border-radius: 0px 10px 10px 0px;
        }
    }
    form{
        display: flex;
        flex-flow: column;
        gap: .5em;
    }
    .form_group{
        display: flex;
        flex-flow: column;
        gap: .25em;
        button{
            width: 6em;
        }
    }
}




</style>