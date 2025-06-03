from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        widgets = {
            'photo': forms.ClearableFileInput(attrs={
                'class': ' mb-4 file:bg-blue-500 file:text-white file:px-4 file:py-2 file:rounded file:border-none'
            })
        }