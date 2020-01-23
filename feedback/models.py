from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Feedback(models.Model):
    """ A feedback posting """
    title = models.CharField(max_length=56, blank=False)
    description = models.TextField(blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title

class FeedbackComment(models.Model):
    """Re-Boot Member Feedback Comments"""
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=256, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return '{0}: {1}'.format(self.feedback.title, self.creator.username)