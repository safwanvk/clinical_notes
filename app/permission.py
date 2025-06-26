from strawberry.permission import BasePermission

class IsAuthenticated(BasePermission):
      message = "Authentication required"

      def has_permission(self, source, info, **kwargs) -> bool:
            return bool(info.context)
