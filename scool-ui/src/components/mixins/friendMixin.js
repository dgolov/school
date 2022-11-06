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
            for (let friend of myFriends) {
                if (friend.profile_id === profileID) {
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

        connect(notification_type, message) {
            this.createNotificationSocket = new WebSocket(
                this.$store.state.webSocketUrl + '/ws/notifications/' + this.id + '/'
            );
            this.createNotificationSocket.onopen = () => {
                this.status = "connected";
                this.createNotificationSocket.send(JSON.stringify(
                    {
                        'notification_type': notification_type,
                        'from_user': this.$store.state.authUser.user,
                        'message': message
                    })
                )
                this.createNotificationSocket.close()
            }
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
                    this.$store.state.profileInfo.friend_request_out.push(this.user);
                    this.connect(
                        'ADD REQUEST',
                        `${this.$store.state.authUser.last_name} 
                                ${this.$store.state.authUser.first_name} хочет добавить Вас в друзья.`
                        )
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
                    this.$store.state.profileInfo.followers.push(this.user)
                    for(let i = 0; i < this.$store.state.profileInfo.friends.length; i++) {
                        if (this.$store.state.profileInfo.friends[i] === this.user) {
                            this.$store.state.profileInfo.friends.splice(i, 1);
                        }
                    }
                    this.connect(
                        'REMOVE FRIEND',
                        null
                    )
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
                    this.$store.state.profileInfo.friends.push(this.user);
                    for(let i = 0; i < this.$store.state.profileInfo.followers.length; i++) {
                        if (this.$store.state.profileInfo.followers[i] === this.user) {
                            this.$store.state.profileInfo.followers.splice(i, 1);
                        }
                    }
                    for(let i = 0; i < this.$store.state.profileInfo.friend_request_in.length; i++) {
                        if (this.$store.state.profileInfo.friend_request_in[i] === this.user) {
                            this.$store.state.profileInfo.friend_request_in.splice(i, 1);
                        }
                    }
                    this.connect('ACCEPT REQUEST', null)
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
                    this.connect('UNSUBSCRIBE', null)
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