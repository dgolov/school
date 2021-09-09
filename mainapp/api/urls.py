from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    StudentsViewSet,
    TeachersViewSet,
    PersonalProfileView,
    ProfileCreateView,
    FriendRequestView,
    FriendResponseView,
    CategoryListView,
    CoursesViewSet,
    LessonsDetailView,
    TimetableViewSet,
    CertificateViewSet,
    AcademicPerformanceViewSet,
    UploadPhotoView,
    UploadAvatarView,
    LikePhotoView,
)


router = routers.SimpleRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('teachers', TeachersViewSet, basename='teachers')
router.register('courses', CoursesViewSet, basename='courses')
router.register('timetable', TimetableViewSet, basename='timetable')
router.register('certificates', CertificateViewSet, basename='certificates')
router.register('performance', AcademicPerformanceViewSet, basename='performance')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', PersonalProfileView.as_view(), name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='create_profile'),
    path('profile/upload-photo', UploadPhotoView.as_view(), name='upload_photo'),
    path('profile/upload-avatar', UploadAvatarView.as_view(), name='upload_avatar'),
    path('profile/like-photo', LikePhotoView.as_view(), name='like-photo'),
    path('profile/add-friend-request', FriendRequestView.as_view(), name='add-friend-request'),
    path('profile/add-friend-response', FriendResponseView.as_view(), name='add-friend-response'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('courses/<int:course_pk>/lessons/<int:pk>', LessonsDetailView.as_view(), name='lesson_detail'),
]
urlpatterns += router.urls
