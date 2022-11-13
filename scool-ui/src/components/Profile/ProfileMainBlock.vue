<template>
  <div class="item">
    <table>
      <tr>
        <td>День рождения:</td>
        <td>{{ profile.date_of_birthday }}</td>
      </tr>
      <tr>
        <td>Пол:</td>
        <td v-if="profile.gender === 'm'">Мужской</td>
        <td v-else>Женский</td>
      </tr>
    </table>
  </div>
</template>


<script>
export default {
  name: "StudentAbout",

  props: ['profile'],
}
</script>


<style scoped>

</style>