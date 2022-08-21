<template>
  <div id="app">
      <component :is="layout"></component>
  </div>
</template>

<script>
    export default {
        computed: {
            layout(){
                return this.$route.meta.layout || "default-layout" 
            }
        }
    }
</script>