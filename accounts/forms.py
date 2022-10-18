from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser
from django import forms


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class":"myfield"}))
    first_name = forms.CharField(label='Введите имя', widget=forms.TextInput(attrs={"class":"myfield"}))
    last_name = forms.CharField(label='Введите фамилию', widget=forms.TextInput(attrs={"class":"myfield"}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={"class":"myfield"}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={"class":"myfield"}))


    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)
        widgets = {
            'email': forms.EmailInput(attrs={"class":"myfield"}),
            'first_name': forms.TextInput(attrs={"class":"myfield"}),
            'last_name': forms.TextInput(attrs={"class":"myfield"}),
        }

    def clean_password2(self) -> str:
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return data['password2']
