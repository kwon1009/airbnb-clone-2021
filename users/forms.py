from django import forms
from . import models


class LoginForm(forms.Form):

    """ Login Form Definition """

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)  # get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist."))


class SignUpForm(forms.Form):

    """ Sign up Form Definition """

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            raise forms.ValidationError("User already exists with that email.")
        except models.User.DoesNotExist:
            return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password_check = self.cleaned_data.get("password_check")

        if password != password_check:
            raise forms.ValidationError("password confirmation does not match.")
        else:
            return password