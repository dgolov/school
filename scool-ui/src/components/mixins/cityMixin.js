export const cityMixin = {
    data() {
        return {
            getCity: false,
        }
    },

    methods: {
        openCity() {
            this.getCity = !this.getCity;
        },

        setCity(city) {
            this.$store.commit('setCity', {city: city})
            if (city === 'Нижний Новгород') {
                this.$store.commit( 'setAddress', {address: 'г. Нижний Новгород, Большая Печерская 40'});
                this.$store.commit( 'setWA', {wa: 'https://wa.me/79050113226?text='});
                this.$store.commit( 'setVB', {vb: 'https://viber.click/79050113226'});
            } else if (city === 'Дзержинск') {
                this.$store.commit( 'setAddress', {address: 'г. Дзержинск, пл. Дзержинского 2'});
                this.$store.commit( 'setWA', {wa: 'https://wa.me/79870864156?text='});
                this.$store.commit( 'setVB', {vb: 'https://viber.click/79870864156'});
            } else {
                this.$store.commit( 'setAddress', {address: null});
                this.$store.commit( 'setWA', {wa: 'https://wa.me/79870864156?text='});
                this.$store.commit( 'setVB', {vb: 'https://viber.click/79870864156'});
            }
            this.getCity = false
        },
    }
}