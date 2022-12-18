import Vue from 'vue'
import VueRouter from 'vue-router'

import Auth from "../views/Auth";
import Profile from "../views/Profile/Profile";
import MyCourses from "../views/Profile/MyCourses";
import CourseSingle from "../views/Profile/CourseSingle";
import Lesson from "../views/Profile/Lesson";
import TimeTable from "../views/Profile/TimeTable";
import TimeTableDetail from "../views/Profile/TimeTableDetail";
import AcademicPerformance from "../views/Profile/AcademicPerformance";
import Chats from "../views/Messages/Chats";
import Messages from "../views/Messages/Messages";
import Friends from "../views/Profile/Friends";
import Followers from "../views/Profile/Followers";
import Groups from "../views/Groups/Groups";
import GroupSingle from "../views/Groups/GroupSingle";
import Search from "../views/Profile/Search";
import Photo from "../views/Profile/Photo";
import MyProfile from "../views/Profile/MyProfile";
import Achievement from "../views/Profile/Achievement";
import Subscriptions from "../views/Profile/Subscriptions";
import FriendRequests from "../views/Profile/FriendRequests";
import CreateGroupChat from "../views/Messages/CreateGroupChat";
import Settings from "../views/Profile/Settings";
import Games from "../views/Profile/Games";
import GroupChatSettings from "../views/Messages/GroupChatSettings";
import PageNotFound from "../views/PageNotFound"
import ForgotPassword from "../views/Profile/ForgotPassword"
import ResetPassword from "../views/Profile/ResetPassword"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MyProfile',
    component: MyProfile,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/auth',
    name: "Auth",
    component: Auth,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profiles/:id',
    name: 'Profile',
    component: Profile,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/my-courses',
    name: 'MyCourses',
    component: MyCourses,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/timetable',
    name: 'TimeTable',
    component: TimeTable,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/timetable/:id',
    name: 'TimeTableDetail',
    component: TimeTableDetail,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/chats',
    name: 'Chats',
    component: Chats,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/chats/:id',
    name: 'Messages',
    component: Messages,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/chats/:id/settings',
    name: 'GroupChatSettings',
    component: GroupChatSettings,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: "/profile/chats/create-group",
    name: 'CreateGroupChat',
    component: CreateGroupChat,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profiles/:id/friends',
    name: 'Friends',
    component: Friends,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profiles/:id/followers',
    name: 'Followers',
    component: Followers,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profiles/:id/subscriptions',
    name: 'Subscriptions',
    component: Subscriptions,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/friend-requests',
    name: 'FriendRequests',
    component: FriendRequests,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profiles/:id/photo',
    name: 'Photo',
    component: Photo,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/groups',
    name: 'Groups',
    component: Groups,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/groups/:id',
    name: 'GroupSingle',
    component: GroupSingle,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/search',
    name: 'Search',
    component: Search,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/settings',
    name: 'Settings',
    component: Settings,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/games',
    name: 'Games',
    component: Games,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/academic-performance',
    name: 'AcademicPerformance',
    component: AcademicPerformance,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/my-courses/:id',
    name: 'CourseSingle',
    component: CourseSingle,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/my-courses/:courseId/lesson/:lessonId',
    name: 'Lesson',
    component: Lesson,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/:id/achievement',
    name: 'Achievement',
    component: Achievement,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/forgot-password',
    name: 'ForgotPassword',
    component: ForgotPassword,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: '/profile/reset-password/:token',
    name: 'ResetPassword',
    component: ResetPassword,
    props: true,
    meta:{
      layout: "082022-layout"
    }
  },
  {
    path: "*",
    component: PageNotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: '/profiles',
  routes
})

export default router
