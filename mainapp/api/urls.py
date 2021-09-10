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
    BuyingACourseView,
    LessonsDetailView,
    TimetableViewSet,
    CertificateViewSet,
    AcademicPerformanceViewSet,
    UploadPhotoView,
    DeletePhotoView,
    UploadAvatarView,
    SetAvatarView,
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
    path('profile/delete-photo/<int:pk>', DeletePhotoView.as_view(), name='delete_photo'),
    path('profile/upload-avatar', UploadAvatarView.as_view(), name='upload_avatar'),
    path('profile/set-avatar', SetAvatarView.as_view(), name='set_avatar'),
    path('profile/like-photo', LikePhotoView.as_view(), name='like-photo'),
    path('profile/friend-request', FriendRequestView.as_view(), name='friend-request'),
    path('profile/friend-response', FriendResponseView.as_view(), name='friend-response'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('courses/buy', BuyingACourseView.as_view(), name='buy-course'),
    path('courses/<int:course_pk>/lessons/<int:pk>', LessonsDetailView.as_view(), name='lesson_detail'),
]
urlpatterns += router.urls
