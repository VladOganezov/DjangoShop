from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя:", widget=forms.TextInput(attrs={"class":"myfield"}))
    last_name = forms.CharField(label="Фамилия:", widget=forms.TextInput(attrs={"class":"myfield"}))
    email = forms.EmailField(label="Email:", widget=forms.EmailInput(attrs={"class":"myfield"}))
    address = forms.CharField(label="Адрес:", widget=forms.TextInput(attrs={"class":"myfield"}))
    postal_code = forms.CharField(label="Почтовый индекс:", widget=forms.TextInput(attrs={"class":"myfield"}))
    city = forms.CharField(label="Населённый пункт:", widget=forms.TextInput(attrs={"class":"myfield"}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
