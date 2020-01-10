from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsWalletUser(BasePermission):
    """
    Allows access only to Manager users.
    """
    message = "برای مشاهده باید وارد حساب کاربری خود شوید"

    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            return True
        else:
            self.message = "برای مشاهده باید وارد حساب کاربری خود شوید"
            return False
