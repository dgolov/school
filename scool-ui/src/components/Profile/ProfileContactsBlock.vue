<template>
  <div class="item">
    <p>Контактная информация:</p>
    <table>
      <tr>
        <td>Телефон:</td>
        <td><a :href="`tel:${ profile.phone }`">{{ profile.phone }}</a></td>
      </tr>
      <tr>
        <td>Город:</td>
        <td v-if="profile.city">{{ profile.city }}</td>
        <td v-else>Не указан</td>
      </tr>
      <tr>
        <td>E-mail:</td>
        <td><a :href="`mailto:${ profile.email }`">{{ profile.email }}</a></td>
      </tr>
      <tr>
        <td>Профиль VK:</td>
        <td><a v-if="profile.vk_slug" :href="`${ profile.vk_slug }`">{{ profile.vk_slug }}</a></td>
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