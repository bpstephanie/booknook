from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import DeliveryDetailsForm, PersonalInfoForm


# Create your views here.
@login_required
def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    delivery_form = DeliveryDetailsForm(instance=profile)
    personal_info_form = PersonalInfoForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'delivery_form': delivery_form,
        'personal_info_form': personal_info_form,
    }
    return render(request, template, context)


@login_required
def update_delivery_details(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = DeliveryDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return redirect('profile')


@login_required
def update_personal_info(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return redirect('profile')
