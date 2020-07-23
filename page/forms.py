from django import forms
from .models import MbtiUser

class PostForm(forms.ModelForm) :
    class Meta:
        model = MbtiUser
        fields = ('id', 'mbti1', 'region', 'age', 'sex',)
