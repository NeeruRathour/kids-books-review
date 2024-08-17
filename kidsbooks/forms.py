from django import forms
from .models import Kidsbook, Review


class KidsbookForm(forms.ModelForm):
    """
    Create a form inherited from forms.ModelForm class
    model: Kidsbook
    """
    class Meta:
        model = Kidsbook
        fields = ('title', 'author', 'price', 'ages', 'image',
                  'description',)


class ReviewForm(forms.ModelForm):
    """
    Create a review form class based on model Review inherited
    from ModelForm module
    model: Review
    """
    class Meta:
        model = Review
        fields = ('content',)

