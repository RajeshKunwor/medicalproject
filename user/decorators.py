from django.contrib.auth.decorators import user_passes_test
from django.utils import six
from django.core.exceptions import PermissionDenied




def superuser_only(function):

    """Limit view to superusers only."""

    def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied
       return function(request, *args, **kwargs)
    return _inner




def group_required(group,raise_exception='False'):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        # First check if the user has the permission (even anon users)

        if user.groups.filter(name__in=groups).exists()|user.is_superuser():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url='login')