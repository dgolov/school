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
                    if (error.request.status === 403 && error.request.responseText === this.errorAccessToken) {
                        // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
                        console.log(1)
                        this.refreshToken()
                        this.createGetRequest(url)
                    }
                })
            if (url === `/profile/${this.$store.state.authUser.id}` || url === '/profile') {
                // Если запрос данных профиля, то сохраняем их в state
                this.$store.commit("setProfileInfo", this.responseData);
            }
        },

        async refreshToken() {
            /* Обновление токена */
            console.log(2)
            const body = {
                'refresh': this.$store.getters.getRefreshJWT
            };
            await axios
                .post(`${this.$store.state.backendUrl}/token/refresh/`, body)
                .then(response => {
                    this.$store.commit("updateToken", response.data.access)
                })
                .catch((error) => {
                    if (error.request.status === 403) {
                        // Если 403 ошибка - refresh токен просрочен, LogOut
                        this.$store.commit("removeToken")
                        this.goTo('/')
                    }
                })
        }
    }
}