from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
User = get_user_model() 

class IsCompanyAdmin(BasePermission):

    def has_permission(self, request, view):
        """check if object has permission"""

        role = request.user.role
        if role == 'CA':
            return True
        else:
            return False