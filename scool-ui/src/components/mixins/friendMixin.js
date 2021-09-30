// Действия связанные с добавлением/удалением друзей, подписками/отписками
import axios from "axios";
import {requestsMixin} from "./requestsMixin";


export const friendMixin = {
    data() {
        return {
            id: 0,
            user: 0
        }
    },

    mixins: [requestsMixin],

    methods: {
        setUserData(profile, mode) {
            //  В некоторых запросах с backend приходит модель User
            //  (в случаях просмотра списка друзей, подписчиков и подписок),
            //  а в некоторых (в основных случаях) приходит связанная с ней модель Profile
            // В зависимости от результата устанавливается режим mode обработки данных,
            // который определяет с какими данными манипулировать в методах
            if (mode === 'profile') {
                this.id = profile.id
                this.user = profile.user
            } else {
                this.id = profile.profile_id
                this.user = profile.id
            }
        },

        isFriend(profileID) {
            const myFriends = this.$store.state.profileInfo.friends
            // Проверяет является ли пользователь другом
            // myFriends - список друзей текущего пользователя
            for (let friendId of myFriends) {
                if (friendId === profileID) {
                    return true;
                }
            }
            return false;
        },

        isFollower(profileID) {
            const myFollowers = this.$store.state.profileInfo.followers
            // Проверяет является ли пользователь подписчиком
            // myFollowers - список подписчиков текущего пользователя
            for (let followerId of myFollowers) {
                if (followerId === profileID) {
                    return true;
                }
            }
            return false;
        },

        isSubscription(profileID) {
            const mybSubscriptions = this.$store.state.profileInfo.friend_request_out
            // Проверяет подписан ли текущий пользователь на пользователя
            // mybSubscriptions - список подписок текущего пользователя
            for (let subscriptionId of mybSubscriptions) {
                if (subscriptionId === profileID) {
                    return true;
                }
            }
            return false;
        },

        async addFriend(profile, mode) {
            // Отправить заявку на добавление в друзья
            this.setUserData(profile, mode)
            let body = {
                'id': this.id
            };
            const axiosInstance = axios.create(this.base);
            await axiosInstance({
                url: '/profile/friend-request/',
                method: "post",
                data: body,
            })
                .then(() => {
                    let subscriptions = this.$store.state.profileInfo.friend_request_out;
                    subscriptions.push(this.user);
                    this.$emit('reLoad')
                })
                .catch((error) => {
                    if (error.request.status === 401) {
                        // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
                        this.refreshToken();
                        this.addFriend('/profile/friend-request/');
                    } else {
                        console.log(error.request);
                    }
                })
        },

        async removeFriend(profile, mode) {
            // Удалить из друзей
            this.setUserData(profile, mode)
            let body = {
                'id': this.id
            };
            const axiosInstance = axios.create(this.base);
            await axiosInstance({
                url: '/profile/friend-response/',
                method: "delete",
                data: body,
            })
                .then(() => {
                    let followers = this.$store.state.profileInfo.followers
                    followers.push(this.user)
                    let friends = this.$store.state.profileInfo.friends
                    for(let i = 0; i < friends.length; i++) {
                        if (friends[i] === this.user) {
                            friends.splice(i, 1);
                        }
                    }
                    this.$emit('reLoad')
                })
                .catch((error) => {
                    if (error.request.status === 401) {
                        // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
                        this.refreshToken()
                        this.addFriend('/profile/friend-response/')
                    } else {
                        console.log(error.request)
                    }
                })
        },

        async addFriendRequest(profile, mode) {
            // Принять заявку в друзья
            this.setUserData(profile, mode)
            let body = {
                'id': this.id,
                "answer": "add"
            };
            const axiosInstance = axios.create(this.base);
            await axiosInstance({
                url: '/profile/friend-response/',
                method: "post",
                data: body,
            })
                .then(() => {
                    let friends = this.$store.state.profileInfo.friends;
                    friends.push(this.user);
                    let followers = this.$store.state.profileInfo.followers;
                    for(let i = 0; i < friends.length; i++) {
                        if (followers[i] === this.user) {
                            followers.splice(i, 1);
                        }
                    }
                    let requests = this.$store.state.profileInfo.friend_request_in
                    for(let i = 0; i < requests.length; i++) {
                        if (requests[i] === this.user) {
                            requests.splice(i, 1);
                        }
                    }
                    this.$emit('reLoad')
                })
                .catch((error) => {
                    if (error.request.status === 401) {
                        // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
                        this.refreshToken()
                        this.addFriend('/profile/friend-response/')
                    } else {
                        console.log(error.request)
                    }
                })
        },

        async unsubscribe(profile, mode) {
            // Отписаться
            this.setUserData(profile, mode)
            let body = {
                'id': this.id
            };
            const axiosInstance = axios.create(this.base);
            await axiosInstance({
                url: '/profile/friend-request/',
                method: "delete",
                data: body,
            })
                .then(() => {
                    let subscriptions = this.$store.state.profileInfo.friend_request_out
                    for(let i = 0; i < subscriptions.length; i++) {
                        if (subscriptions[i] === this.user) {
                            subscriptions.splice(i, 1);
                        }
                    }
                    this.$emit('reLoad')
                })
                .catch((error) => {
                    if (error.request.status === 401) {
                        // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
                        this.refreshToken()
                        this.addFriend('/profile/friend-request/')
                    } else {
                        console.log(error.request)
                    }
                })
        },
    },
}