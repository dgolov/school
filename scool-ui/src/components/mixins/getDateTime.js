export const getDateTime = {
    methods: {
        reformatDateTime(dateTime) {
            // Приводит полученную дату с сервера к удобному формату
            let now = new Date();
            let reformattedDate = ''
            let dateTimeList = dateTime.split('T')
            let dateList = dateTimeList[0].split('-')
            let time = dateTimeList[1].substring(0, 5)

            for (let date of dateList) {
                if (reformattedDate) {
                    reformattedDate = `${date}.${reformattedDate}`
                } else {
                    reformattedDate = date
                }
            }
            return `${reformattedDate} ${time}`
        },
    }
}