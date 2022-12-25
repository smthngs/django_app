from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="kullanıcı adı")
    password = forms.CharField(max_length=100, label="parola", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("kullanıcı adı")
        password = self.cleaned_data.get("parola")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adı veya parola yanlış!")
        return super(LoginForm, self).clean()


GEEKS_CHOICES = (
    ('Evet', 'Evet'),
    ('Hayır', 'Hayır'),
)
GEEKS_CHOICES2 = (
    ('Erkek', 'Erkek'),
    ('Kadın', 'Kadın'),
)


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label=("Parola"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=""
    )
    password2 = forms.CharField(
        label=("Parola doğrulaması"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=(
                      "Parolanı doğrulamak için tekrar gir.") + "\n" + password_validation.password_validators_help_text_html()

    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Girdiğiniz parolalar uyuşmuyor!")
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user
