// Миксин для групповых бесед

export const groupChatMixin = {
    methods: {
        getAvatarPath(friend){
            // Отображает аватарки пользователей в настройках и создании бесед
            let path = ''
            if (friend.avatar) {
                path = `http://127.0.0.1:8000${friend.avatar}`;
            } else {
                path = require('../../assets/images/avatars/mike2.jpeg');
            }
            return path;

        },
    }
}