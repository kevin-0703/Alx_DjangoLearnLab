from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Write your comment here...",
                "class": "form-control",
            }),
        }
        def clean_content(self):
            content = self.cleaned_data.get('content')
            if not content or content.strip() == "":
                raise forms.ValidationError("Comment content cannot be empty.")
            if len(content) > 500:
                raise forms.ValidationError("Comment content cannot exceed 500 characters.")
            return content