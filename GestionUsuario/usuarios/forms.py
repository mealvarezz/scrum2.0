from django import forms
from django.contrib.auth import  get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    organization_id = forms.IntegerField(
        required=True, widget=forms.TextInput(attrs={"autofocus": True})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Invalid username, password.",
                    code="invalid_login",
                )

        return self.cleaned_data

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','email']