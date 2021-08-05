from django import forms
from .models import Goods


class NewForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = ('title', 'text', 'img',)
