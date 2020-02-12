from django import forms
from .models import NewImage


class AddNewImage(forms.ModelForm):

    class Meta:
        model = NewImage
        fields = ('image',)
        labels = {
            'image': (''),
        }
