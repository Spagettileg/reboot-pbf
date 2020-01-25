from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Feedback, FeedbackComment
from django.utils import timezone
from django.contrib import messages
from .forms import FeedbackCommentForm, FeedbackCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def show_all_feedbacks(request):
    
    """
    View to show all our features on one page
    """
    feedback_list = Feedback.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    page = request.GET.get('page', 1)
    
    paginator = Paginator(feedback_list, 5)
    
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        feedbacks = paginator.page(1)
    except EmptyPage:
        feedbacks = paginator.page(paginator.num_pages)
    
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'feedback.html', context)

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
def create_a_feedback(request):
    """
    Route to allow Re-boot members to create feedback 
    """
    form = FeedbackCreationForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.creator = request.user
            feedback.save()
            messages.success(request, "Thank you {0}, {1} has been added."
                             .format(request.user, feedback.title),
                             extra_tags="alert-primary")
            return redirect('profile')
    else:
        form = FeedbackCreationForm()
        messages.error(request, '{} sorry, your feedback cannot be added.'.format(request.user), extra_tags="alert-primary")
    
    context = {
        'form' : form
    }
    
    return render(request, 'create_feedback.html', context)
    
@login_required
def edit_a_feedback(request, pk):
    """
    Route to permit Re-Boot members to edit their feedback
    """
    feedback = get_object_or_404(Feedback, pk=pk)
    
    if request.method == "POST":
        form = FeedbackCreationForm(request.POST, instance=feedback)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.creator = request.user
            feedback.save()
            messages.success(request, "Thank you {0}, {1} has been updated."
                             .format(request.user, feedback.title),
                             extra_tags="alert-primary")
            return redirect(reverse('profile'))
    
    else:
        form = FeedbackCreationForm(instance=feedback)
        messages.error(request, '{} sorry, your feedback cannot be updated.'.format(request.user), extra_tags="alert-primary")
        
    context = {
        'form': form,
    }
    return render(request, 'edit_feedback.html', context)

@login_required
def delete_a_feedback(request, pk):
    """
    Route to allow Re-Boot members to delete their feedback
    """
    
    feedback = get_object_or_404(Feedback, pk=pk)
    
    if request.method == "POST":
        feedback.delete()
        messages.success(request, '{} your feedback has been deleted!'.format(request.user), extra_tags="alert-success")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, '{} sorry, your feedback cannot be deleted.'.format(request.user), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))