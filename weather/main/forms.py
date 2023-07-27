from django.forms import ModelForm, Select

from .models import mockDb

class WeatherForm(ModelForm):
    class Meta:
        model = mockDb
        fields = ['city']
        CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
        date = mockDb.objects.all()
        widgets = {
            'city': Select(attrs={'class': 'form-select', 'onchange': 'submit();'}, choices=CHOICES)
		}