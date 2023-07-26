from django.forms import ModelForm, ChoiceField

from .models import mockDb

class WeatherForm(ModelForm):
    class Meta:
        model = mockDb
        fields = ['city']
        
        widgets = {
            'city': ChoiceField(attrs={'class': 'form-select'})
		}
        