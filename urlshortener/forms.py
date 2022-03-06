from django import forms;
from django.core import validators;

from .models import Shortener;

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control form-control-lg", "placeholder": "Sua URL para ser encurtada" }),
        required=True
        )

    class Meta:
        model = Shortener;
        fields = ('long_url',)

    def clean(self):
        super(ShortenerForm, self).clean()

        long_url = self.cleaned_data.get('long_url')
        validators.URLValidator()(long_url)

        return self.cleaned_data