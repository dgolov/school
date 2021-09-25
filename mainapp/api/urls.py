from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    UserRetrieveView,
    StudentsViewSet,
    TeachersViewSet,
    PersonalProfileView,
    ProfileCreateView,
    FriendRequestView,
    FriendResponseView,
    FriendsListView,
    OutRequestsListView,
    InRequestsListView,
    FollowersListView,
    GroupViewSet,
    CategoryListView,
    CoursesViewSet,
    BuyingACourseView,
    LessonsDetailView,
    TimetableViewSet,
    AcademicPerformanceViewSet,
    CertificateViewSet,
    GalleryListView,
    EditPhotoDescription,
    UploadPhotoView,
    DeletePhotoView,
    UploadAvatarView,
    SetAvatarView,
    LikePhotoView,
    DialogViewSet,
    CreateAGroupDialog,
    SendMessageView,
)


router = routers.SimpleRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('teachers', TeachersViewSet, basename='teachers')
router.register('groups', GroupViewSet, basename='groups')
router.register('courses', CoursesViewSet, basename='courses')
router.register('timetable', TimetableViewSet, basename='timetable')
router.register('certificates', CertificateViewSet, basename='certificates')
router.register('performance', AcademicPerformanceViewSet, basename='performance')
router.register('dialogs', DialogViewSet, basename='dialogs')


urlpatterns = [
    # Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserRetrieveView.as_view(), name='user'),
    # Profile
    path('profile/<int:pk>/', PersonalProfileView.as_view(), name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='create_profile'),
    path('profile/<int:pk>/friends/', FriendsListView.as_view(), name='friends'),
    path('profile/<int:pk>/followers/', FollowersListView.as_view(), name='followers'),
    path('profile/<int:pk>/subscriptions/', OutRequestsListView.as_view(), name='subscriptions'),
    path('profile/friend-requests/', InRequestsListView.as_view(), name='friend_requests'),
    path('profile/friend-request/', FriendRequestView.as_view(), name='friend-request'),
    path('profile/friend-response/', FriendResponseView.as_view(), name='friend-response'),
    path('profile/<int:pk>/gallery/', GalleryListView.as_view(), name='gallery'),
    path('profile/edit-photo/', EditPhotoDescription.as_view(), name='edit_photo'),
    path('profile/upload-photo/', UploadPhotoView.as_view(), name='upload_photo'),
    path('profile/delete-photo/<int:pk>/', DeletePhotoView.as_view(), name='delete_photo'),
    path('profile/upload-avatar/', UploadAvatarView.as_view(), name='upload_avatar'),
    path('profile/set-avatar/', SetAvatarView.as_view(), name='set_avatar'),
    path('profile/like-photo/', LikePhotoView.as_view(), name='like-photo'),
    # Courses
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('courses/buy/', BuyingACourseView.as_view(), name='buy-course'),
    path('courses/<int:course_pk>/lessons/<int:pk>/', LessonsDetailView.as_view(), name='lesson_detail'),
    # Messages
    path('send-message/', SendMessageView.as_view(), name='send_message'),
    path('create-group-dialog/', CreateAGroupDialog.as_view(), name='create_group_dialog'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
