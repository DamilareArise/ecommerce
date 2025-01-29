from functools import wraps
from django.shortcuts import redirect

def staff_required(view_func):
    @wraps(view_func)
    def wrapped(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapped