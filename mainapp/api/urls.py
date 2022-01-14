from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from mainapp.api import views


router = routers.SimpleRouter()
router.register('profile', views.PersonalProfileView, basename='profile')
router.register('students', views.StudentsViewSet, basename='students')
router.register('teachers', views.TeachersViewSet, basename='teachers')
router.register('groups', views.GroupViewSet, basename='groups')
router.register('courses', views.CoursesViewSet, basename='courses')
router.register('timetable', views.TimetableViewSet, basename='timetable')
router.register('certificates', views.CertificateViewSet, basename='certificates')
router.register('performance', views.AcademicPerformanceViewSet, basename='performance')
router.register('dialogs', views.DialogViewSet, basename='dialogs')
router.register('events', views.EventViewSet, basename='events')
router.register('news', views.NewsViewSet, basename='news')


urlpatterns = [
    # Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.UserRetrieveView.as_view(), name='user'),
    # Profile
    # path('profile/<int:pk>/', PersonalProfileView.as_view(), name='profile'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='create_profile'),
    path('profile/<int:pk>/friends/', views.FriendsListView.as_view(), name='friends'),
    path('profile/<int:pk>/followers/', views.FollowersListView.as_view(), name='followers'),
    path('profile/<int:pk>/subscriptions/', views.OutRequestsListView.as_view(), name='subscriptions'),
    path('profile/friend-requests/', views.InRequestsListView.as_view(), name='friend_requests'),
    path('profile/friend-request/', views.FriendRequestView.as_view(), name='friend-request'),
    path('profile/friend-response/', views.FriendResponseView.as_view(), name='friend-response'),
    path('profile/<int:pk>/gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('profile/edit-photo/', views.EditPhotoDescription.as_view(), name='edit_photo'),
    path('profile/upload-photo/', views.UploadPhotoView.as_view(), name='upload_photo'),
    path('profile/delete-photo/<int:pk>/', views.DeletePhotoView.as_view(), name='delete_photo'),
    path('profile/upload-avatar/', views.UploadAvatarView.as_view(), name='upload_avatar'),
    path('profile/set-avatar/', views.SetAvatarView.as_view(), name='set_avatar'),
    path('profile/like-photo/', views.LikePhotoView.as_view(), name='like-photo'),
    # Courses
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('courses/buy/', views.BuyingACourseView.as_view(), name='buy-course'),
    path('courses/<int:course_pk>/lessons/<int:pk>/', views.LessonsDetailView.as_view(), name='lesson_detail'),
    # Messages
    path('send-message/', views.SendMessageView.as_view(), name='send_message'),
    path('create-group-dialog/', views.CreateAGroupDialog.as_view(), name='create_group_dialog'),
    path('upload-dialog-image/<int:pk>/', views.UploadGroupDialogImage.as_view(), name='upload_dialog_image'),
    path('update-group-chat/<int:pk>/', views.UpdateGroupDialogName.as_view(), name='update_group_chat'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
