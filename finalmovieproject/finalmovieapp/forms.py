from . models import Movie,Comment
from  django import forms

class MovieForm(forms.ModelForm):
    class Meta:
        model= Movie
        fields=['name','desc','date','image','actors','category','youtubelink']
        exclude = ['slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Body': forms.Textarea(attrs={'class': 'form-control'}),
        }