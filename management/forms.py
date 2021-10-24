from django import forms


class AuthForm(forms.Form):
    """ Форма входа пользователя
    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Логин, телефон или email...', 'style': 'width: 96%;'}
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль...', 'style': 'width: 96%;'}
        )
    )
