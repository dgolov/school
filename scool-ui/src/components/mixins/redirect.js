//import {isNavigationFailure} from "vue-router/src/util/errors";
import {NavigationFailureType} from "vue-router";


export const redirect = {
    methods: {
        goTo(view_component, params = {}) {
            // осуществляет переход на заданную страницу с заданными параметрами
            this.$router.push({name: view_component, params: params}).catch(error => {
//                if (!isNavigationFailure(error, NavigationFailureType.duplicated)) {
//                    throw Error(error)
//                }
            })
            window.scrollTo(0,0)
        },
    }
}