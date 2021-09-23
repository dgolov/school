export const redirect = {
    methods: {
        goTo(view_component, params = {}) {
            // осуществляет переход на заданную страницу с заданными параметрами
            this.$router.push({name: view_component, params: params})
        },
    }
}