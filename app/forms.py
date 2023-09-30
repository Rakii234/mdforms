from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['name','password']
        #exclude=['name','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'password':'Create Strong password with length 8'}