import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authUser: {},
    profileInfo: {},
    isAuthenticated: false,
    jwt: localStorage.getItem("token"),
    refreshJwt: localStorage.getItem("refresh_token"),
    refreshStatus: false,
    backendUrl: "/api",
    webSocketUrl: "wss://109.172.27.159:8001",
    isMainPage: false,
    error: '',
  },

  mutations: {
    setAuthUser(state, { authUser, isAuthenticated }) {
      Vue.set(state, "authUser", authUser);
      Vue.set(state, "isAuthenticated", isAuthenticated);
    },
    setProfileInfo(state, { profileInfo }) {
      Vue.set(state, "profileInfo", profileInfo);
    },
    setError(state, { error }) {
      Vue.set(state, "error", error);
    },
    updateToken(state, newToken) {
      // Записывается во время авторизации либо во время обновления токена
      localStorage.setItem("token", newToken);
      state.jwt = newToken;
    },
    updateRefreshToken(state, newToken) {
      // Записывается во время авторизации
      localStorage.setItem("refresh_token", newToken);
      state.refreshJwt = newToken;
    },
    setRefreshStatus(status){
      this.refreshStatus = status
    },
    removeToken(state) {
      localStorage.removeItem("token");
      localStorage.removeItem("refresh_token");
      state.jwt = null;
      state.refreshJwt = null;
      state.isAuthenticated = false;
    },
  },

  actions: {
  },

  modules: {
  },

  getters: {
    getServerUrl: state => {
      return state.backendUrl
    },
    getJWT: state => {
      return state.jwt
    },
    getRefreshJWT: state => {
      return state.refreshJwt
    },
    getRefreshStatus: state => {
      return state.refreshStatus
    },
    getIsAuthenticated: state => {
      return state.isAuthenticated
    },
    getAuthUser: state => {
      return state.authUser
    },
    getProfileInfo: state => {
      return state.profileInfo
    },
  },

  plugins: [createPersistedState()]
})
