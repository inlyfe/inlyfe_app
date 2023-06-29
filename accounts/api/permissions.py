from rest_framework.permissions import BasePermission


class IsVendorUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_vendor)


class IsOfficeUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_office_admin)

class IsReceptionUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_reception)