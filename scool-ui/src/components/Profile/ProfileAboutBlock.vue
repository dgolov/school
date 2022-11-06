<template>
  <div class="item">
    <p>Личная информация:</p>
    <table>
      <tr>
        <td>О себе:</td>
        <td v-if="profile.about">{{ profile.about }}</td>
        <td v-else>Не указано</td>
      </tr>
      <tr v-if="profile.user_group === 'student' && profile.hobbies">
        <td>Увлечения:</td>
        <td>{{ profile.hobbies }}</td>
      </tr>
      <tr v-if="profile.user_group === 'student' && profile.dream">
        <td>Мечта:</td>
        <td>{{ profile.dream }}</td>
      </tr>
      <tr v-if="profile.user_group === 'teacher' && profile.education">
        <td>Образование:</td>
        <td>{{ profile.education }}</td>
      </tr>
      <tr v-if="profile.user_group === 'teacher' && profile.professional_activity">
        <td>Профессиональная деятельность:</td>
        <td>{{ profile.professional_activity }}</td>
      </tr>
    </table>
  </div>
</template>


<script>
export default {
  name: "ProfileAboutBlock",

  props: ['profile'],
}
</script>


<style scoped>

</style>