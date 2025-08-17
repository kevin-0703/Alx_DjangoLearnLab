from django import forms
from .models import Comment, Post
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
        

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas",
        widget=forms.TextInput(attrs={"placeholder": "e.g. django, python, web"})
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Handle tags
            tags_input = self.cleaned_data.get("tags")
            if tags_input:
                tag_names = [t.strip() for t in tags_input.split(",") if t.strip()]
                tags = []
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    tags.append(tag)
                instance.tags.set(tags)
        return instance