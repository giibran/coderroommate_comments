from django import forms

from my_app.models import Comment


class CommentsCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'body', 'is_inappropriate', 'ranking'
        ]

    def save(self, commit=True):
        comment = super(CommentsCreateForm, self).save(commit=False)
        if commit:
            comment.save()
        return comment
