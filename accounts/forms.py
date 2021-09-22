from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='لطفا نام کاربری خود را وارد کنید',
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))

    password = forms.CharField(
        label='لطفا رمز عبور خود را وارد کنید',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='لطفا نام کاربری خود را وارد کنید',
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))

    email = forms.EmailField(
        label='لطفا ایمیل خود را وارد کنید',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))

    password = forms.CharField(
        label='لطفا رمز عبور خود را وارد کنید',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))

    re_password = forms.CharField(
        label='لطفا رمز عبور دوباره خود را وارد کنید',
        widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور'}))
