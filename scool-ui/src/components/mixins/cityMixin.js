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
                this.$store.commit(
                    'setAddress',
                    {address: 'г. Нижний Новгород, Большая Печерская 40'}
                )
            } else if (city === 'Дзержинск') {
                this.$store.commit(
                    'setAddress',
                    {address: 'г. Дзержинск, пл. Дзержинского 2'}
                )
            } else {
                this.$store.commit('setAddress', {address: null})
            }
            this.getCity = false
        },
    }
}