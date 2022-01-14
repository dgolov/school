export const playerMixin = {
    data() {
        return {
            videoLink: true,
            wrapperModal: false,
        }
    },

    methods: {
        videoStart() {
            this.videoLink = false;
            this.wrapperModal = true;
        },
        videoClose() {
            this.videoLink = true;
            this.wrapperModal = false;
        },
    }
}