from django.contrib import admin
from .models import Feedback, FeedbackComment

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'creator', 'created_date']
    list_filter = ('created_date',)
    
class FeedbackCommentAdmin(admin.ModelAdmin):
    list_display = ['feedback', 'comment', 'creator', 'created_date']
    list_filter = ('feedback', 'creator')

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FeedbackComment, FeedbackCommentAdmin)