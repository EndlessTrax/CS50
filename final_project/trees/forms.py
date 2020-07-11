from django.forms import ModelForm

from .models import Tree


class TreeCreationForm(ModelForm):
    class Meta:
        model = Tree
        fields = ["name", "species", "description", "location", "price", "picture"]

