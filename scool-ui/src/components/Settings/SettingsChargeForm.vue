<template>
  <div class="row mt-3">
    <div class="col-md-9 my-2">
      <form>
        <input v-model="value" type='text' class="w-100 input-field" placeholder="">
      </form>
    </div>
    <div class="col-md-3 my-2">
      <button class="gray-button filter-button" style="height: 100%;" @click="setNewValue">Изменить</button>
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
.input-field {
  background-color: #ededed;
  height: 100%;
  border-radius: 5px;
  padding: 10px;
}
</style>