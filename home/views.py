from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ContactForm

def index(request):
    """ A view that displays the index page """
    return render(request, "index.html")


def contact(request):
    
    # Directs the customer to a contact us form
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            to_list = [email_address]
            send_mail(
                subject,
                message,
                from_email,
                to_list,
                fail_silently=False)
            messages.success(
                request,
                """We\'ve received your message,
                and shall be back with you shortly""")
        return redirect('products')
    context = {'contact_form': form}
    return render(request, 'contact.html', context)


def explained(request, *args, **kwargs):
    
    # Directs the customer to Re-Boot explained page
    return render(request, "explained.html", {"home": "explained"})

    
def faqs(request, *args, **kwargs):
    
    # Directs the customer to FAQ'S page
    return render(request, "faqs.html", {"home": "faqs"})

    
def juniors(request, *args, **kwargs):
    
    # Directs the customer to the juniors page, setting out pricing & sizes
    return render(request, "juniors.html", {"home": "juniors"})

    
def adults(request, *args, **kwargs):
    
    # Directs the customer to the adults page, setting out pricing & sizes
    return render(request, "adults.html", {"home": "adults"})
    
def bootquality(request, *args, **kwargs):
    
    # Directs the customer to the boot quality page. Accepted quality standards
    return render(request, "bootquality.html", {"home": "bootquality"})
    
def cookie(request, *args, **kwargs):
    
    # Directs the customer to the cookie page. User guidance notes
    return render(request, "cookie.html", {"home": "cookie"})