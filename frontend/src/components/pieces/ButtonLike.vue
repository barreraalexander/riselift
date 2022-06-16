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

<script>

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

<style scoped>
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
}

.button_like:hover{
  cursor: pointer;
}
.button_like img{
  width: 2em;
}
.button_like p {
  color: #fff;
}
</style>
