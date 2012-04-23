from django.forms import ModelForm

from places.models import Place,Comment

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        exclude = ["slug","thumb"]
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["place"]