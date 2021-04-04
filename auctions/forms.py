from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class BidForm(forms.Form):
    bid = forms.FloatField()