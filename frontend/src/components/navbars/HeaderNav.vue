<template>
  <section id="HeaderSection">
    <nav>
      <img
        src="../../assets/images/icons/kaiyote1.svg"
        class="logo"
        alt=""
      >
      <div class="nav_ctnr">
        <ul>
          <li>
            <router-link to="/">Home</router-link>
          </li>
          <li>
            <router-link to="/about">About</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <!-- <router-view/> -->
  </section>
</template>

<style lang="scss">

@import "../../assets/scss/navbars/HeaderNav.scss";


</style>