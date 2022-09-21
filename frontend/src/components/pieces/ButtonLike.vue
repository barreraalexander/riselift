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

export default{
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
}


</script>

<style lang="scss">
@import "../../assets/scss/pieces/ButtonLike.scss"
</style>
