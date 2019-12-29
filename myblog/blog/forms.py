from django import forms
from . models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'blog_title', 'text')

    widgets = {
        'blog_title': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'textinputclass'})
    }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('author','text')

    widgets = {
        'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'textinputclass'})
    }