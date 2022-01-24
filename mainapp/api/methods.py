def get_normalize_phone(phone: str) -> (str, None):
    """ Приводит телефонный номер к стандартному виду
    :param phone: номер телефона введенный пользователем
    :return: Отредактированный номер телефона
    """
    if not phone:
        return None
    if len(phone) in (10, 11):
        if len(phone) == 11 and phone.startswith('8'):
            return '+7' + phone[1:]
        elif len(phone) == 11 and phone.startswith('7'):
            return '+' + phone
        elif len(phone) == 10 and phone.startswith('9'):
            return '+7' + phone
    elif len(phone) == 12 and phone.startswith('+7'):
        return phone
    else:
        return None
