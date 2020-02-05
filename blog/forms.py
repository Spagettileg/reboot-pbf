from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Below are editable fields
        fields = ('title', 'content', 'image', 'tag', 'published_date')
