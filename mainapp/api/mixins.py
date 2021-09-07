from rest_framework.views import APIView


class ProfileAPIViewMixin(APIView):
    def get_profile(self):
        return self.request.user.profile
