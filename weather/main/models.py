import datetime
from django.db import models
from django.utils import timezone

class Cities(models.Model):
    city = models.CharField(verbose_name='Название', default='Мурманск', max_length=30)
    
    def	__str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    

class Weather(models.Model):
    city = models.ForeignKey(verbose_name='Выбрать город', to=Cities, on_delete = models.CASCADE)
    date = models.DateTimeField(verbose_name='Выбрать день и время')
    t = models.IntegerField(verbose_name='Температура')

    def	__str__(self):
        ret_time = timezone.localtime(self.date)
        time = ret_time.time()
        select_time = time.strftime('%H:%M')
        select_date = datetime.datetime.strftime(self.date, "%d.%m.%Y")
        return f'Город: {self.city} Дата: {select_date} Время: {select_time}'
    
    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода'

