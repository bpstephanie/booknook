from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, 'info/about.html')


def contact(request):
    return render(request, 'info/contact.html')


def faqs(request):
    return render(request, 'info/faqs.html')


def terms_and_conditions(request):
    return render(request, 'info/terms.html')
