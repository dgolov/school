from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.views import APIView

from mainapp.models import Photo


class ProfileManagerMixin(APIView):
    """ Миксин передающий значение текущего пользователя """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def get_profile(self):
        return self.request.user.profile

    def add_photo(self, request, *args, **kwargs):
        user = self.get_profile()
        up_file = request.FILES['image']
        new_photo = Photo.objects.create(image=up_file)
        user.photos.add(new_photo)
        return new_photo
