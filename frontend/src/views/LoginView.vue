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

import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent ({
    name: "LoginView",
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
        async handleSubmit(e: Event){
            e.preventDefault()
            var bodyFormData = new FormData()
            bodyFormData.append(
                'username', this.email
            )

            bodyFormData.append(
                'password', this.password
            )

            let result = await axios.post('http://localhost:5000/login', bodyFormData)
         
            let request_config = {
                headers: {
                    Authorization: `Bearer ${result.data.access_token}`

                }
            }
        
            console.log(request_config)


            let current_user = await axios.get('http://localhost:5000/users/current', request_config)
            console.log(current_user)

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