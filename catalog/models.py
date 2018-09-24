from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
#
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from django.http import HttpResponse
from datetime import datetime
from slugify import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse_lazy

# Create your models here.

class Author(models.Model):
    """
    Описание таблицы профиля автора.
    """
    first_name = models.CharField(max_length=100, help_text="Укажите Вашу Фамилию", verbose_name="Фамилия")
    last_name = models.CharField(max_length=100, help_text="Укажите Ваше Имя", verbose_name="Имя")
    otch_name = models.CharField(max_length=100, help_text="Укажите Ваше Отчество, если есть", verbose_name="Отчество")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Дата рождения", verbose_name="Дата рождения")
    photo_author = models.ImageField(upload_to = 'photo/%Y/%m/%d', max_length=256, verbose_name="Ваше фото", blank=True, null=True, validators=[validate_file_extension])
    gorod = models.CharField(max_length=100, help_text="От куда Вы, Название населенного пункта", verbose_name="Откуда:")
    sport_razyad = models.CharField(max_length=6, help_text="Спортивный разряд", verbose_name="Разряд")
    sudeyskaja_kategorija = models.CharField(max_length=6, help_text="Судейская категория, если есть", verbose_name="Категория")
    fn_sportsmena = models.CharField(max_length=7, help_text="Ваш федеральный номер спортсмена (если есть)", verbose_name="федеральный номер")
    author_hobby = models.TextField(max_length=3000, help_text="Ваши интересы или дополнительная информация о себе", verbose_name="Ваши интересы или дополнительная информация")
    author_site = models.CharField(max_length=100, help_text="Адрес Вашего сайта или ссылка на профиль в социальных сетях", verbose_name="Ваш сайт или ссылка на профиль в соц сетях")
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s  %s %s' % (self.last_name, self.otch_name, self.first_name)

#----------------------------------------------------------------------------------------------------------#
#
#
#----------------------------------------------------------------------------------------------------------#
class Ship_model(models.Model):
    """
    Здесь описываю собственно судомодель копию, со всеми ее характеристиками
    """
    ship_name = models.CharField(max_length=100, help_text="Название модели", verbose_name="Название модели")
    photo_modelship = models.ImageField(upload_to = 'ship/%Y/%m/%d', max_length=256, verbose_name="Фото модели", blank=True, null=True,validators=[validate_file_extension])
    ship_prototype = models.TextField(max_length=1200, help_text="Описание прототпа, № проекта, год постройки и т.д.", verbose_name="Прототип, описание")
    photo_prototype = models.ImageField(upload_to = 'ship_prototype/%Y/%m/%d', max_length=256, verbose_name="Фото прототипа", blank=True, null=True, validators=[validate_file_extension])
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, verbose_name="Автор", null=True)
    ship_scale = models.CharField(max_length=5, help_text="В каком масштабе вполнена модель", verbose_name="Масштаб 1:")
    # Перечисляю классы по NAVIGA
    NAVIGA_CLASS = (
        ('---', 'Класс модели не оперделен'),
        ('F2A', 'F2-A - масштабные копийные модели, длина которых не превышает 900 мм'),
        ('F2B', 'F2-B - масштабные копийные модели, длина которых составляет от 901 до 1400 мм '),
        ('F2С', 'F2-C - масштабные копийные модели, длина которых не менее 1401 мм '),
        ('F2S', 'F2-S - масштабные копийные модели подводных лодок'),
        ('Ф2Ю', 'Ф2-Ю - Масштабные копийные модели, длина которых не превышает 600 мм'),
        ('F4А', 'F4-A - Модели, выполненные из любых наборов или полностью готовые'),
        ('F4B', 'F4-B - модели, выполненные из композитных наборов, которые проходят и стендовую, и ходовую оценки.'),
        ('F4С', 'F4-C - модели, выполненные из пластмассы, литой под давлением, которые должны проходить и стендовую, и ходовую оценки.'),
        ('FDS', 'F-DS - точные радиоуправляемые модели - копии паровых кораблей, судов и катеров'),
        ('NSS-A', 'NSS-A масштабные копийные модели c парусным вооружением типа - бермудский шлюп'),
        ('NSS-B', 'NSS-B масштабные копийные модели c парусным вооружением типа - гафельный парус'),
        ('NSS-С', 'NSS-C масштабные копийные модели c парусным вооружением типа - прямые паруса'),
        ('NSS-D', 'NSS-D масштабные копийные модели - много корпусные парусники'),
        )
    
    ship_class_naviga = models.CharField(max_length=30, help_text="Класс по NAVIGA", verbose_name="NAVIGA Класс", choices=NAVIGA_CLASS, blank=True, default='---')
     #Технологии (выбор из списка)
    TEHNOLOGY = (
        ('Не использовались', 'Инновации не использовались, в основном ручное производство'),
        ('Использовались', 'Использовались современные технологии проектирования и изготовления деталей'),
        ('Набор', 'Модель из набора'),
        )
    
    ship_tehnology = models.CharField(max_length=30, help_text="Используемые инновационные технологии", verbose_name="инновационные технологии", choices=TEHNOLOGY, blank=True, default='Не использовались')
    #Даты постройки
    date_start = models.DateField(null=True, blank=True, help_text="Дата начала постройки", verbose_name="Дата начала постройки")
    #date_end = models.DateField(null=True, blank=True, help_text="Дата окончания постройки", verbose_name="Дата окончания постройки")
    #-------------
    #Стендовая оценка - автором
    ship_stend = models.CharField(max_length=3, help_text="Баллы на стенде", verbose_name="Авторская стендовая оценка")
    #Стендовая оценка - судейской бригадой
    ship_stend_refery = models.CharField(max_length=3, help_text="Баллы на стенде", verbose_name="Судейская стендовая оценка")
    #Ходовая оценка
    ship_run = models.CharField(max_length=3, help_text="Баллы за ход", verbose_name="Баллы за хода")
    #
    # статус модели
    STATUS = (
        ('не определен', 'статус не указан'),
        ('Строится', 'В процесе постройки'),
        ('Готова', 'Процесс постройки завершон'),
        ('Не исправна', 'Не исправна или выработан ресурс'),
        ('Утрачена', 'модель утрачена, утонула, разбита и т.д.'),
        ('Продана', 'У модели новый владелец'),
        )
    
    ship_status = models.CharField(max_length=30, help_text="Текущий статус модели", verbose_name="Определите статус", choices=STATUS, blank=True, default='не определен')
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s - %s    %s' % (self.ship_name, self.author, self.ship_class_naviga)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular ship instance.
        """
        return reverse('ship-detail', args=[str(self.id)])

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
