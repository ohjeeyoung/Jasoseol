from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 부모 class 가져와서 쓸 수 있음
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder': '제목',
        })

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
