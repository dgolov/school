from mainapp.api.serializers import ProfileSerializer


def get_serializer_to_display_the_profile(request, obj, detail_serializer_class):
    """
        Выбор серилизатора для режима отображения профиля.
        Если пользователь в друзьях, то используется детальный серилизатор, иначе серилизатор с не полной информацией.
        Информация о профиле показывается только друзьям пользователя
    """
    item_profile = request.user.profile
    if obj.user in item_profile.friends.all() and request.user in obj.friends.all():
        serializer = detail_serializer_class(obj, many=False)
    else:
        serializer = ProfileSerializer(obj, many=False)
    return serializer
