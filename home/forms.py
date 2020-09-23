from django import forms


class ContactForm(forms.Form):
    """
    Form for contact-page uses sendgrid API
    """

    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget = forms.Textarea()
    )

    class Meta:
        fields = [
            'name',
            'email',
            'message',
        ]