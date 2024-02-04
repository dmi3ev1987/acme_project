# birthday/views.py
# from django.shortcuts import render, get_object_or_404, redirect
# Импортируем класс пагинатора.
# from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
# from .utils import calculate_birthday_countdown
# Импортируем модель дней рождения.
from .models import Birthday


class BirthdayMixin:
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Этот класс сам может создать форму на основе модели!
    # Нет необходимости отдельно создавать форму через ModelForm.
    # Указываем поля, которые должны быть в форме:
    # fields = '__all__'
    # Указываем имя формы:
    form_class = BirthdayForm
    # Явным образом указываем шаблон:
    template_name = 'birthday/birthday.html'
    # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # после создания объекта:
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(BirthdayMixin, CreateView):
    pass


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass


# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10/2


class BirthdayDeleteView(DeleteView):
    model = Birthday
    # Убириаем эту строку т.к. создан новый шаблон с стандартным именем
    # template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')
