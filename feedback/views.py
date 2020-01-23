from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Feedback, FeedbackComment
from django.utils import timezone
from django.contrib import messages
from .forms import FeedbackCommentForm, FeedbackCreationForm
from django.contrib.auth.decorators import login_required

def show_all_feedbacks(request):
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, "feedback.html", context)

def single_feature_view(request, pk):
    """
    Route to view a single feature on
    one page
    """
    feature = get_object_or_404(Feature, pk=pk)
    
    if request.method == 'POST':
        feature_comment_form = FeatureCommentForm(request.POST or None)
        if feature_comment_form.is_valid():
            comment = request.POST.get('comment')
            feature_comment = FeatureComment.objects.create(feature=feature, creator=request.user, comment=comment)
            feature_comment.save()
            messages.success(request, 'Thanks {} your comment has posted'.format(request.user), extra_tags="alert-success")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        feature_comment_form = FeatureCommentForm()
        feature.views += 1
        feature.save()
    
    comments = FeatureComment.objects.filter(feature=feature)
    
    feature_comment_form = FeatureCommentForm()
            
    context = {
        'feature' : feature,
        'feature_comment_form': feature_comment_form,
        'comments': comments,
    }
    
    
    return render(request, 'single_feature.html', context)
    
    
@login_required
def create_a_feature(request):
    """
    Route to allow our users to create a feature
    """
    form = FeatureCreationForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            feature = form.save(commit=False)
            feature.creator = request.user
            feature.save()
            
            cart = request.session.get('cart', {})
            id = feature.id
            cart[id] = cart.get(id, 1)
            request.session['cart'] = cart
            return redirect('checkout')
    else:
        form = FeatureCreationForm()
    
    context = {
        'form' : form
    }
    
    return render(request, 'create_feature.html', context)
    
@login_required
def edit_a_bug(request, pk):
    """
    Route to allow users to edit their bugs
    """
    bug = get_object_or_404(Bug, pk=pk)
    
    if request.method == "POST":
        form = BugCreationForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.creator = request.user
            bug.save()
            messages.success(request, "Thanks {0}, {1} has been updated."
                             .format(request.user, bug.title),
                             extra_tags="alert-primary")
            return redirect(reverse('profile'))
    
    else:
        form = BugCreationForm(instance=bug)
        
    context = {
        'form': form,
    }
    return render(request, 'edit_bug.html', context)

@login_required
def delete_a_feature(request, pk):
    """
    Route to allow users to delete their features
    """
    
    feature = get_object_or_404(Feature, pk=pk)
    
    if request.method == "POST":
        feature.delete()
        messages.success(request, '{} your feature has been deleted!'.format(request.user), extra_tags="alert-success")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, '{} unfortunatley at this time your feature cannot be deleted.'.format(request.user), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))