<template>
  <section id="HeaderSection">
    <h1>
      hi
    </h1>  
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </section>
</template>

<style lang="scss">
#HeaderSection{
  background: $primary;
  h1{
    color: #fff;
  }

}
</style>