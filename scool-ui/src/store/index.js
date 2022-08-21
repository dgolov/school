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
    ageGroup: 'children',
    refreshJwt: localStorage.getItem("refresh_token"),
    refreshStatus: false,
    backendUrl: "/api",
    webSocketUrl: "wss://109.172.27.159:8001",
    isMainPage: false,
    error: '',
    city: 'Дзержинск',
    phone: '8 800 550 09 72',
    address: 'г. Дзержинск, пл. Дзержинского 2',
    wa: 'https://wa.me/79870864156?text=',
    vb: 'https://viber.click/79870864156',
    
  },

  mutations: {
    setAuthUser(state, { authUser, isAuthenticated }) {
      Vue.set(state, "authUser", authUser);
      Vue.set(state, "isAuthenticated", isAuthenticated);
    },
    setProfileInfo(state, { profileInfo }) {
      Vue.set(state, "profileInfo", profileInfo);
    },
    setCity(state, { city }) {
      Vue.set(state, "city", city);
    },
    setAddress(state, { address }) {
      Vue.set(state, "address", address);
    },
    
    setWA(state, { wa }) {
      Vue.set(state, "wa", wa);
    },
    
    setVB(state, { vb }) {
      Vue.set(state, "vb", vb);
    },
    
    setAgeGroup(state, { ageGroup }) {
      Vue.set(state, "ageGroup", ageGroup);
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
