from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import UserProfile
# from .forms import UserProfileForm


# Create your views here.
@login_required
def profile(request):
    """
    Display user's profile
    """
    # user_profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        # 'user_profiles': user_profile,
    }
    return render(request, template, context)


"""
@login_required
def profile_update(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.methos == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profiles_update.html', {'form': form})
"""