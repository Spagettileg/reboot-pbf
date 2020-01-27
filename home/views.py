from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ContactForm

def index(request):
    """ A view that displays the index page """
    return render(request, "index.html")


def contact(request):
    """
    Directs the customer to a contact us form
    """
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