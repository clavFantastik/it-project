from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=12, min_length=4)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        field = ['username', 'password']

class SignUpForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=12, min_length=4)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        field = ['email', 'username', 'password1', 'password2']
