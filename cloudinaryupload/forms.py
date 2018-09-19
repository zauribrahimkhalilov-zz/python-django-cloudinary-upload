from django import forms
from cloudinaryupload.models import ImageUpload


class UploadForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        fields = ['image']