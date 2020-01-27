from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea()
    )

    class Meta:
        fields = [
            'name', 'subject', 'email_address', 'message'
        ]