from django.shortcuts import render
from django.contrib import messages
from .forms import NewsletterSignupForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.
def send_newsletter_signup_email(name, email):
    subject = render_to_string('home/emails/newsletter_signup_subject.txt')
    body = render_to_string(
        'home/emails/newsletter_signup_body.txt', {'name': name})
    plain_body = strip_tags(body)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, plain_body, from_email, recipient_list)


def index(request):
    """ A view that displays the index page """
    form = NewsletterSignupForm()
    return render(request, 'home/index.html', {'form': form})


def newsletter_signup(request):
    """ A view that displays the newsletter signup """
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            signup = form.save()
            send_newsletter_signup_email(signup.name, signup.email)
            messages.success(
                request,
                'Thank you for signing up to the BookNook Newsletter!')
        else:
            messages.error(
                request,
                'Oops! Looks that email has already been signed up.')
    else:
        form = NewsletterSignupForm()
    return render(request, 'home/index.html', {'form': form})
