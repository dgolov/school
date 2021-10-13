// Действия происходящие на стороне клиента (с которым проводим операции), отправка ему сигнала о наших действиях
// через веб сокеты

export const vebSocketMixin = {
    methods: {
        parseNotificationData(data) {
            data = JSON.parse(data);
            switch (data.notification_type) {
                // Заявка на добавление в друзья
                case "ADD REQUEST": {
                    this.$store.state.profileInfo.friend_request_in.push(data.from_user);
                    this.$store.state.profileInfo.followers.push(data.from_user);
                    break;
                }
                // Удаление из друзей
                case "REMOVE FRIEND": {
                    this.$store.state.profileInfo.friend_request_out.push(data.from_user)
                    for(let i = 0; i < this.$store.state.profileInfo.friends.length; i++) {
                        if (this.$store.state.profileInfo.friends[i] === data.from_user) {
                            this.$store.state.profileInfo.friends.splice(i, 1);
                        }
                    }
                    break;
                }
                // Подтверждение дружбы
                case "ACCEPT REQUEST": {
                    this.$store.state.profileInfo.friends.push(data.from_user);
                    for(let i = 0; i < this.$store.state.profileInfo.friend_request_out.length; i++) {
                        if (this.$store.state.profileInfo.friend_request_out[i] === data.from_user) {
                            this.$store.state.profileInfo.friend_request_out.splice(i, 1);
                        }
                    }
                    break;
                }
                // Отписка
                case "UNSUBSCRIBE": {
                    for(let i = 0; i < this.$store.state.profileInfo.followers.length; i++) {
                        if (this.$store.state.profileInfo.followers[i] === data.from_user) {
                            this.$store.state.profileInfo.followers.splice(i, 1);
                        }
                    }
                    for(let i = 0; i < this.$store.state.profileInfo.friend_request_in.length; i++) {
                        if (this.$store.state.profileInfo.friend_request_in[i] === data.from_user) {
                            this.$store.state.profileInfo.friend_request_in.splice(i, 1);
                        }
                    }
                    break;
                }
            }
        },
    }
}