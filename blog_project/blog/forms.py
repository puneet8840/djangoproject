from django import forms
from blog.models import Comment

class Mail(forms.Form):
    name=forms.CharField(max_length=10)
    From=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
class CommentForm(forms.ModelForm):
    body=forms.CharField(label="COMMENT",required=True,widget=forms.Textarea(attrs={'class':"textarea",'name':"body"}))
    class Meta:
        model=Comment
        fields=('name','email','body')
