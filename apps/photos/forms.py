from django.forms import ModelForm

from models import Photo


class PhotoForm(ModelForm):
    """
    Form for creating and updating photos with user excluded as it should be set automatically from request.
    """
    class Meta:
        model = Photo
        exclude = ('user',)

