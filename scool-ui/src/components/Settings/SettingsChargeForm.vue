<template>
  <div class="row mt-3">
    <div class="col-md-9">
      <form>
        <input v-model="value" type='text' class="w-100">
      </form>
    </div>
    <div class="col-md-3">
      <button class="gray-button filter-button" style="height: 68%;" @click="setNewValue">Изменить</button>
    </div>
  </div>
</template>


<script>
export default {
  name: "SettingsChargeForm",

  data() {
    return {
      value: ''
    }
  },

  methods: {
    setNewValue(){
      this.$emit('setValue', {value: this.value})
      this.value = ''
    }
  }
}
</script>


<style scoped>

</style>