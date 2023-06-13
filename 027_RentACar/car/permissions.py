from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True
        # elif request.user.is_staff:
        #     return True
        # else:
        #     return False
        return request.method in SAFE_METHODS or request.user.is_staff


class IsStaffOrOnlyOwnerObjects(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.id == obj.user.id
