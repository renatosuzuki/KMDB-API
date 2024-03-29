from rest_framework import permissions

class IsGetOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return bool(request.user.is_superuser)