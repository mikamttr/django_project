from django.shortcuts import redirect


def login_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('connexion')
    return wrapped_view
