from django.views import generic
from my_app import forms
from my_app import models


class IndexView(generic.ListView):
    template_name = 'my_app/index.html'
    model = models.Comment
    context_object_name = "comments"


class CommentCreateView(generic.CreateView):
    template_name = 'my_app/create_comment.html'
    form_class = forms.CommentsCreateForm
    success_url = '/'
