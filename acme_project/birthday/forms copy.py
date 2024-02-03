# birthday/forms.py
from django import forms

# Импортируем функцию-валидатор.
from .validators import real_age


class BirthdayForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'}),
        # В аргументе validators указываем список или кортеж
        # валидаторов этого поля (валидаторов может быть несколько).
        validators=(real_age,),
    )
