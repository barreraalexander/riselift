<template>
    <div class="button_like">
      <img
        src="../../assets/images/icons/bolt.svg"
        alt=""
      />
      <p>
        {{types["demo"]["label"]}}
      </p>
    </div>
  </template>
  
  <script lang="ts">
import { defineComponent } from "vue"

  
  export default defineComponent({
    data: () => ({
      valid: true,
      types: {
        "demo" : {
          'label' : 'DEMO',
          'img_src' : '../../assets/bolt.svg'
        },
        "call" : {
          'label' : '9548828507',
          'img_src' : '../../assets/bolt.svg'
        },
      }
    }),
    props: {
      message: { required: true, type: String }
    }
  })  
</script>

<style lang="scss">

.button_like {
    /* box-shadow: 1px 4px 10px 3px #c8c8c8; */
    align-items: center;
    justify-content: center;
    gap: .5em;
    display: flex;
    border-radius: 20px;
    background: #222;
    padding: .5em .75em;
    width: 10em;
    font-size: .8em;
    img{
        width: 2em;
    }
    p{
        color: #fff;
    }
  }
  
  .button_like:hover{
    cursor: pointer;
  }


</style>