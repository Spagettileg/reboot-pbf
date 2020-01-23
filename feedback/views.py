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

def single_feedback_view(request, pk):
    """
    Route to view a single feedback on one page
    """
    feedback = get_object_or_404(Feedback, pk=pk)
    
    if request.method == 'POST':
        feedback_comment_form = FeedbackCommentForm(request.POST or None)
        if feedback_comment_form.is_valid():
            comment = request.POST.get('comment')
            feedback_comment = FeedbackComment.objects.create(feedback=feedback, creator=request.user, comment=comment)
            feedback_comment.save()
            messages.success(request, 'Thank you {} your feedback has posted'.format(request.user), extra_tags="alert-success")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        feedback_comment_form = FeedbackCommentForm()
        feedback.views += 1
        feedback.save()
    
    comments = FeedbackComment.objects.filter(feedback=feedback)
    
    feedback_comment_form = FeedbackCommentForm()
            
    context = {
        'feedback' : feedback,
        'feedback_comment_form': feedback_comment_form,
        'comments': comments,
    }
    
    
    return render(request, 'single_feedback.html', context)
    
    
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