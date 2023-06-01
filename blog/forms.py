from django import forms
from .models import Comments



class CommentForm(forms.ModelForm):


    class Meta:
        model = Comments
        fields = ['which_post', 'name', 'email', 'subject', 'message']
        
        