import axios from "axios";
import {redirect} from "./redirect";


export const requestsMixin = {
    data() {
        return {
            base: {
                baseURL: this.$store.state.backendUrl,
                headers: {
                    Authorization: `Bearer ${this.$store.state.jwt}`,
                    "Content-Type": "application/json",
                },
                xhrFields: {
                    withCredentials: true,
                },
            },
            responseData: {},
            errorAccessToken: '{"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"AccessToken","token_type":"access","message":"Token is invalid or expired"}]}'
        }
    },

    mixins: [redirect],

    methods: {
        async createGetRequest(url) {
            const axiosInstance = axios.create(this.base);

            await axiosInstance({
                url: url,
                method: "get",
                params: {},
            })
                .then((response) => this.responseData = response.data)
                .catch((error) => {
                    if (error.request.status === 403) {
                        // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
                        if (!this.$store.getters.getRefreshStatus) {
                            // Повторный запрос выполнится при статусе обновления токена false
                            this.$store.commit('setRefreshStatus', true);   // Ставим статус обновления токена
                            let newToken = this.refreshToken();
                            if (newToken) {
                                this.$store.commit('setRefreshStatus', false);
                                this.createGetRequest(url)
                            }
                        }
                    }
                })
            if (url === `/profile/${this.$store.state.authUser.id}/`) {
                // Если запрос данных профиля, то сохраняем их в state
                this.$store.commit("setProfileInfo", {profileInfo: this.responseData});
            }
        },

        async refreshToken() {
            /* Обновление токена */
            const body = {
                'refresh': this.$store.getters.getRefreshJWT
            };
            let access = ''
            await axios
                .post(`${this.$store.state.backendUrl}/token/refresh/`, body)
                .then(response => {
                    this.$store.commit("updateToken", response.data.access)
                    access = response.data.access
                    this.base.headers.Authorization = `Bearer ${access}`
                })
                .catch((error) => {
                    if (error.request.status === 403) {
                        // Если 403 ошибка - refresh токен просрочен, LogOut
                        this.$store.commit("removeToken")
                        this.goTo('/')
                    }
                })
            return access
        }
    }
}