from rest_framework import status


class NoAuthorisationJWT:
    """ Перехват непонятного статус-кода 403 при отсутствии авторизации и корректировка на нужный 401
    """
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self._get_response(request)
        try:
            if response.data['detail'] == 'Given token not valid for any token type':
                response.status_code = status.HTTP_401_UNAUTHORIZED
        except Exception:
            # Другие запросы имеют иную структуру, поэтому исключения игнорируем
            pass

        return response
