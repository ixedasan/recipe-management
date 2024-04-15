from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'peer h-full shadow-lg w-full rounded-[7px] border bg-transparent px-3 py-2.5 pr-20 font-sans text-sm font-normal text-orange-500 outline outline-0 transition-all placeholder-shown:border focus:border-2 focus:border-orange-500 focus:border-t-transparent focus:outline-0'}),
            'first_name': forms.TextInput(attrs={
                'class': 'peer h-full shadow-lg w-full rounded-[7px] border bg-transparent px-3 py-2.5 pr-20 font-sans text-sm font-normal text-orange-500 outline outline-0 transition-all placeholder-shown:border focus:border-2 focus:border-orange-500 focus:border-t-transparent focus:outline-0'}),
            'last_name': forms.TextInput(attrs={
                'class': 'peer h-full shadow-lg w-full rounded-[7px] border bg-transparent px-3 py-2.5 pr-20 font-sans text-sm font-normal text-orange-500 outline outline-0 transition-all placeholder-shown:border focus:border-2 focus:border-orange-500 focus:border-t-transparent focus:outline-0'}),
            'password1': forms.PasswordInput(attrs={
                'class': 'peer h-full shadow-lg w-full rounded-[7px] border bg-transparent px-3 py-2.5 pr-20 font-sans text-sm font-normal text-orange-500 outline outline-0 transition-all placeholder-shown:border focus:border-2 focus:border-orange-500 focus:border-t-transparent focus:outline-0'}),
            'password2': forms.PasswordInput(attrs={
                'class': 'peer h-full shadow-lg w-full rounded-[7px] border bg-transparent px-3 py-2.5 pr-20 font-sans text-sm font-normal text-orange-500 outline outline-0 transition-all placeholder-shown:border focus:border-2 focus:border-orange-500 focus:border-t-transparent focus:outline-0'}),
        }
