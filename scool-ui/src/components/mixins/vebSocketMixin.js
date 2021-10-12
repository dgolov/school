export const vebSocketMixin = {
    methods: {
        parseNotificationData(data) {
            data = JSON.parse(data);
            switch (data.notification_type) {
                case "ADD REQUEST": {
                    this.$store.state.profileInfo.friend_request_in.push(data.from_user);
                    this.$store.state.profileInfo.followers.push(data.from_user);
                    break;
                }
            }
        },
    }
}