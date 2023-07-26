from django.db import models

class mockDb(models.Model):
    city = models.CharField('Название', default='Мурманск', max_length=30)
    t = models.CharField('Температура', default='0', max_length=2)
    date = models.DateField('Дата')
    
    def	__str__(self):
        return self.city