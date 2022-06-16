<script setup>
import axios from 'axios';

</script>


<template>

<section id="RegisterModal">
    <h2>
        Register
    </h2>
    <form id="register_form" action="">

        <div class="form_group">
            <label for="email">
                Email
            </label>
            <input
                type="text"
                v-model="email"
                placeholder="james@gmail.com"
            >
        </div>

        <div class="form_group">
            <label for="password">
                Password
            </label>
            <input
                type="password"
                v-model="password"
            >
        </div>

        <div class="form_group">
            <button @click="submitRegister">
                Register Now
            </button>
        </div>

    </form>
</section>

</template>

<script>
// import axios from 'axios'


export default {
    data: () => ({
        valid: true,
        email: "",
        password: "",

    }),
    methods: {
        async submitRegister(event){
            if (event){
                event.preventDefault()
                let result = await axios.post('http://localhost:5000/users', {
                    email: this.email,
                    password: this.password
                })
                let form = document.querySelector('#register_form')
                form.reset()
                console.log(result)

            }




        }
    }
}


</script>
