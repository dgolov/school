<template>
<div id="groups">
  <navbar></navbar>
  <div class="step landing__section main-section past-events">
    <div class="page">
      <div class="container mt-1">
        <div class="page__inner">
          <profile-menu :header="header"></profile-menu>
          <div class="page__main">
            <group-search></group-search>
            <groups-header></groups-header>
            <hr/>
            <div v-for="group in responseData" class="row row_list mt-3">
              <div class="w-50">
                <a href="#" class="left-align" @click="goTo('GroupSingle', {id: group.id})">
                  {{ group.name }}
                </a>
              </div>
              <div class="w-50">
                <a href="#" class="left-align" @click="goTo('Profile', {id: group.teacher.id})">
                  {{ group.teacher.last_name }} {{ group.teacher.first_name }} {{ group.teacher.middle_name }}
                </a>
              </div>
            </div>
            <h6 v-if="responseData.length === 0" class="mt-5">Вы не состоите ни в одной группе</h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import GroupsHeader from "../../components/Groups/GroupsHeader";
import GroupSearch from "../../components/Groups/GroupSearch";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

export default {
  name: "MyGroups",

  components: {
    GroupsHeader, GroupSearch, Navbar, ProfileMenu
  },

  data() {
    return {
      header: 'Группы'
    }
  },

  mixins: [requestsMixin, redirect],

  created() {
    this.createGetRequest('/groups/')
  },
}
</script>


<style scoped>

</style>