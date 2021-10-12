from rest_framework import permissions


class IsFriendOrMyself(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    # def has_object_permission(self, request, view, obj):
    #     if request.user.profile != profile and item_user not in profile.friends.all():
    #
    #     return False
