<template>
  <div class="row row_list">
    <div class="col-name left-align">{{ itemLabel }}:</div>
    <div class="col-value left-align">{{ itemValue }}</div>
    <div class="col-change">
      <button class="system-color button-charge" @click="showForm('LastNameForm')">Изменить</button>
    </div>
    <settings-charge-form v-if="isShowForm" @setValue="setValue"></settings-charge-form>
  </div>
</template>


<script>
import SettingsChargeForm from "./SettingsChargeForm";

export default {
  name: "SettingsField",

  data() {
    return {
      isShowForm: false,
      itemValue: '',
      itemLabel: '',
    }
  },

  props: ['value', 'label'],

  created() {
    this.itemValue = this.value;
    this.itemLabel = this.label;
  },

  components: {SettingsChargeForm},

  methods: {
    showForm() {
      this.isShowForm = !this.isShowForm;
    },

    setValue(data) {
      this.itemValue = data.value
      this.$emit('setValue', {value: this.itemValue})
      this.isShowForm = false;
    },
  },
}
</script>


<style scoped>
.col-name {
  margin-top: 10px;
  color: gray;
  width: 30%;
}

.col-value {
  margin-top: 10px;
  width: 50%;
}

.col-change {
  width: 20%;
}

.button-charge {
  border: none;
  background: none;
  margin: 0;
  font-size: 14px;
  width: 100%;
}
</style>