from django.forms import ModelForm
from .models import Author, Ship_model

class AuthorForm(ModelForm):
  class Meta:
    model = Author
    fields = ['photo_author']

class Ship_modelForm(ModelForm):
  class Meta:
    model = Ship_model
    fields = ['photo_modelship', 'photo_prototype']
