from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Full name *', widget=forms.TextInput({'placeholder': 'Enter your full name'}), required=True)
    email_address = forms.EmailField(label='Email address *', widget=forms.TextInput({'placeholder': 'Enter your email'}), required=True)
    subject = forms.CharField(label='Subject *', widget=forms.TextInput({'placeholder': 'Add your subject'}), required=True)
    message = forms.CharField(label='Your enquiry *', widget=forms.Textarea({'placeholder': 'Enter your message'}), required=True)

    class Meta:
        fields = [
            'name', 'subject', 'email_address', 'message'
        ]