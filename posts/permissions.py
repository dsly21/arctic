from django.contrib.auth.decorators import user_passes_test


def superuser_required(view_func=None, redirect_field_name=None, login_url='/login', message=None):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, displaying message if provided.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser and u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        # message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
