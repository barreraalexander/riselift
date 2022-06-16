<template>

<section id="LoginModal">
    <div class="login_ctnr lightshadow">
        
        <h2>
            Login Form
        </h2>

        <form id="login_form" action="" enctype="multipart/form-data">
            <div class="form_ctnr">

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
                    <button @click="submit">
                        submit
                    </button>
                </div>
                
            </div>
        </form>
  </div>
  
  </section>
</template>


<script>
import axios from 'axios';

export default {
  data: () => ({
    valid: true,
    email: "",
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    password: "",
  }),
  methods: {
    async submit(e) {
        e.preventDefault();


        var bodyFormData = new FormData()

        let form = document.querySelector('#login_form')
        // console.log(form)

        bodyFormData.append(
            'username', this.email
        )

        bodyFormData.append(
            'password', this.password
        )

        console.log(bodyFormData)
        // return
        // axios.defaults.headers.post['Content-Type'] = 'multipart/form-data';

        let result = await axios.post('http://localhost:5000/login', bodyFormData)

        // let result = await axios.post('http://localhost:5000/login', {
        //     data: form,
        //     headers: {
        //         "Content-Type": "multipart/form-data",
        //     }
        // })
        console.log(result)
        form.reset()
    },
    validate () {
    },
    reset (e) {
        e.preventDefault();
        this.password = ""
        this.email = ""
    },
    resetValidation () {
    },

  },

};
</script>



<style scoped>
#LoginModal {
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  height: 100vh;
  width: 100vw;
  z-index: 100;
  color: #fff;
}

.login_ctnr {
  background-color: #222;
  border-radius: 20px;
  height: 90%;
  max-height: 40em;
  padding: 2em 0.5em;
  max-width: 40em;
  width: 80%;
}

h2 {
  text-align: center;
}

.form_ctnr{
    display: flex;
    flex-flow: column;
    gap: 2em;
}

button{
    width: 10em;
}

.form_group {
  display: flex;
  flex-flow: column;
  gap: 0.25em;
}

input {
  width: 75%;
  max-width: 25em;
}
</style>
