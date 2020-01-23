from django import forms
from .models import FeedbackComment, Feedback

class FeedbackCommentForm(forms.ModelForm):
    class Meta:
        model = FeedbackComment
        fields = ('comment',)
        
class FeedbackCreationForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('title', 'description')