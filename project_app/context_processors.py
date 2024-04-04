def logged_in_username(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return {'logged_in_username': username}
