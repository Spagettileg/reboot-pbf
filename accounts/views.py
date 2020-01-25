from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from products.models import Product
from feedbacks.models import Feedback 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def register(request):
    
    """
    Render the registration page
    """
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in", 
                         extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
        
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, 
                               "Unable to register your account at this time!",
                               extra_tags="alert-primary")
    else:
        # Create an instance of reg form
        registration_form = UserRegistrationForm()  
        
    return render(request, 'registration.html', {
        "registration_form": registration_form})
    """
    registration_form passed through as a context dictionary.
    """


def login(request):
    
    """
    Return a Login page
    """
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in!", 
                         extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
            password = request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!", 
                                 extra_tags="alert-primary")
                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required    
def logout(request):
    
    """
    Log the user out
    """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!", 
                     extra_tags="alert-primary")
    return redirect(reverse('index'))


@login_required()
def profile(request):
    
    """User profile page"""
    user = User.objects.get(email=request.user.email)
    feedback_list = Feedback.objects.filter(creator=user.id)
    page = request.GET.get('page', 1)
    
    feedback_paginator = Paginator(feedback_list, 2)
    
    try:
        feedbacks = feedback_paginator.page(page)
    except PageNotAnInteger:
        feedbacks = feedback_paginator.page(1)
    except EmptyPage:
        feedbacks = feedback_paginator.page(feedback_paginator.num_pages)
    
    context = {
        'profile': user,
        'feedbacks': feedbacks,
    }
    
    return render(request, 'profile.html', context)
