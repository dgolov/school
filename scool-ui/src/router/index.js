import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Auth from "../views/Auth";
import Profile from "../views/Profile/Profile";
import Education from "../views/Education";
import EducationSingle from "../views/EducationSingle";
import ChessSingleCourse from "../views/ChessSingleCourse";
import Events from "../views/Events";
import About from "../views/About";
import News from "../views/News";
import Contacts from "../views/Contacts";
import MyCourses from "../views/Profile/MyCourses";
import CourseSingle from "../views/Profile/CourseSingle";
import Lesson from "../views/Profile/Lesson";
import TimeTable from "../views/Profile/TimeTable";
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
import Subscriptions from "../views/Profile/Subscriptions";
import FriendRequests from "../views/Profile/FriendRequests";
import CreateGroupChat from "../views/Messages/CreateGroupChat";
import Settings from "../views/Profile/Settings";
import Games from "../views/Profile/Games";
import GroupChatSettings from "../views/Messages/GroupChatSettings";
import EventSingle from "../views/EventSingle";
import Career from "../views/Career";
import Requests from "../views/Requests";
import Reviews from "../views/Reviews";
import Camp from "../views/Camp"
import PageNotFound from "../views/PageNotFound"


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/index.php',
    redirect: { name: 'Home' }
  },
  {
    path: '/index.html',
    redirect: { name: 'Home' }
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/auth',
    name: "Auth",
    component: Auth,
    props: true
  },
  {
    path: '/profile',
    name: 'MyProfile',
    component: MyProfile,
  },
  {
    path: '/profiles/:id',
    name: 'Profile',
    component: Profile,
    props: true
  },
  {
    path: '/profile/my-courses',
    name: 'MyCourses',
    component: MyCourses
  },
  {
    path: '/profile/timetable',
    name: 'TimeTable',
    component: TimeTable
  },
  {
    path: '/profile/chats',
    name: 'Chats',
    component: Chats
  },
  {
    path: '/profile/chats/:id',
    name: 'Messages',
    component: Messages,
    props: true
  },
  {
    path: '/profile/chats/:id/settings',
    name: 'GroupChatSettings',
    component: GroupChatSettings,
    props: true
  },
  {
    path: "/profile/chats/create-group",
    name: 'CreateGroupChat',
    component: CreateGroupChat,
    props: true
  },
  {
    path: '/profiles/:id/friends',
    name: 'Friends',
    component: Friends,
    props: true
  },
  {
    path: '/profiles/:id/followers',
    name: 'Followers',
    component: Followers,
    props: true
  },
  {
    path: '/profiles/:id/subscriptions',
    name: 'Subscriptions',
    component: Subscriptions,
    props: true
  },
  {
    path: '/profile/friend-requests',
    name: 'FriendRequests',
    component: FriendRequests,
  },
  {
    path: '/profiles/:id/photo',
    name: 'Photo',
    component: Photo,
    props: true
  },
  {
    path: '/profile/groups',
    name: 'Groups',
    component: Groups
  },
  {
    path: '/profile/groups/:id',
    name: 'GroupSingle',
    component: GroupSingle,
    props: true
  },
  {
    path: '/profile/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/profile/settings',
    name: 'Settings',
    component: Settings
  },
  {
    path: '/profile/games',
    name: 'Games',
    component: Games
  },
  {
    path: '/profile/academic-performance',
    name: 'AcademicPerformance',
    component: AcademicPerformance
  },
  {
    path: '/profile/my-courses/:id',
    name: 'CourseSingle',
    component: CourseSingle,
    props: true
  },
  {
    path: '/profile/my-courses/:courseId/lesson/:lessonId',
    name: 'Lesson',
    component: Lesson,
    props: true
  },
  {
    path: '/education',
    name: 'Education',
    component: Education,
    props: true
  },
  {
    path: '/education/:slug',
    name: 'EducationSingle',
    component: EducationSingle,
    props: true
  },
  {
    path: '/chess/:slug',
    name: 'ChessSingle',
    component: ChessSingleCourse,
    props: true
  },
  {
    path: '/events',
    name: 'Events',
    component: Events
  },
  {
    path: '/events/:slug',
    name: 'EventSingle',
    component: EventSingle,
    props: true
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
  {
    path: '/news/:slug',
    name: 'NewsSingle',
    component: News,
    props: true
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts
  },
  {
    path: '/career',
    name: 'Career',
    component: Career
  },
  {
    path: '/reviews',
    name: 'Reviews',
    component: Reviews
  },
  {
    path: '/send-request',
    name: 'Requests',
    component: Requests,
    props: true
  },
  {
    path: '/summer-camp',
    name: 'Camp',
    component: Camp,
    props: true
  },
  {
    path: "*",
    component: PageNotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
