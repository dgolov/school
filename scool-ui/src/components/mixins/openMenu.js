
export const openMenu = {
    data() {
        return {
            opened: false
        }
    },

    methods: {
        openProfileMenu() {
            let page = document.getElementsByClassName('cabinet-page');
            let menu = document.getElementsByClassName('menu');

            if (!this.opened){
                page[0].classList.add('opened');
                menu[0].classList.add('opened');
                this.opened = true;
            } else {
                page[0].classList.remove('opened');
                menu[0].classList.remove('opened');
                this.opened = false;
            }
        }
    },
}