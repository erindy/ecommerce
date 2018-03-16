from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control",
               "placeholder": "your full name",
               "id": "form_full_name"}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder": "email",
               "id": "form_email"}))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'your message'
                   }))


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError('Email has to be gmail.com')

        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)