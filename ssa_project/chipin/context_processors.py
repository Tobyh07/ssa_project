from users.models import Profile

def example_processor(request):
    return {"example_key": "example_value"}

def user_profile(request):
    if request.user.is_authenticated:
        try:
            return {'nickname': request.user.profile.nickname}
        except Profile.DoesNotExist:
            return {'nickname': request.user.username}  # Fallback to username if no profile exists
    return {}