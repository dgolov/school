export const dialogMixin = {
    methods: {
        getParticipant(participants) {
            let itemUserId = this.$store.state.authUser.id;
            for (let participant of participants) {
                if (participant.id !== itemUserId) {
                    return participant;
                }
            }
        },

        getChatImage(chat) {
            let path = '';
            if (!chat.is_group) {
                let participant = this.getParticipant(chat.participants);
                try {
                    path = `${this.$store.getters.getServerUrl}${participant.avatar.image}`;
                } catch {
                    path = require('../../assets/images/avatars/mike2.jpeg');
                }
            } else {
                if (chat.image) {
                    path = `${this.$store.getters.getServerUrl}${chat.image.file}`;
                } else {
                    path = require('../../assets/images/group_chat.png');
                }
            }
            return path;
        },

        getChatName(chat) {
            let name = ''
            if (!chat.is_group) {
                let participant = this.getParticipant(chat.participants);
                name = `${participant.first_name} ${participant.last_name}`;
            } else {
                name = chat.name;
            }
            return name;
        },

        getUserId(chat){
            if (chat.is_group) {
                return false;
            }
            let participant = this.getParticipant(chat.participants);
            return participant.id;
        }
    }
}