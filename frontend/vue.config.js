const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      sass: {
        additionalData: `
          @import "@/assets/scss/globals/_variables.scss";
          @import "@/assets/scss/globals/_animations.scss";
          @import "@/assets/scss/globals/_mixins.scss";
        `
      }
    }
  }
})
