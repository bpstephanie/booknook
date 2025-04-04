from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from profiles.models import UserProfile


# Create your views here.
def about(request):
    return render(request, 'info/about.html')


def contact(request):
    """ View to render Contact Us page and receive enquiries"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry received!')
            return redirect('contact_success')
        else:
            messages.error(
                request, 'Please make sure all fields are filled out.')
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = ContactForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': request.user.email
                })
            except UserProfile.DoesNotExist:
                form = ContactForm()
        else:
            form = ContactForm()

    return render(request, 'info/contact.html', {'form': form})


def contact_success(request):
    """ View to render Contact Success Page """
    return render(request, 'info/contact_success.html')


def faqs(request):
    return render(request, 'info/faqs.html')


def privacy_policy(request):
    return render(request, 'info/privacy_policy.html')


def partners(request):
    return render(request, 'info/partners.html')
