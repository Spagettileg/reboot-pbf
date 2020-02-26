from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput
                           ({'placeholder': 'Calling for a hero!'}),
                           required=True)
    """
    Title helps purposes of the blog post stand out and attract a
    response from the Re-Boot community
    """
    author = forms.CharField(widget=forms.TextInput
                            ({'placeholder': 'Martin Johnson'}),
                            required=True)
    """
    ID of the blog post author is important to build good repoire and
    helps Re-Boot in monitoring of blog post quality
    """
    content = forms.CharField(widget=forms.Textarea
                             ({'placeholder': 'Enter your detailed message'}),
                             required=True)
    """
    Important for other users to understand the reason behind the
    blog post. Short and punchy messages tend to work better
    """
    tag = forms.CharField(widget=forms.TextInput
                         ({'placeholder': 'Meta'}),
                         required=True)
    """
    Meta tags are essentially little content descriptors that help tell
    search engines what a web page is about.
    """

    class Meta:
        model = Post
        # Below are editable fields
        fields = ('title', 'author', 'content', 'image', 'tag',
                  'published_date')
