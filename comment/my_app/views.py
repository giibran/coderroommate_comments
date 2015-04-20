from django.views import generic
from my_app import forms


class IndexView(generic.TemplateView):
    template_name = 'my_app/index.html'


class CommentCreateView(generic.CreateView):
    template_name = 'my_app/create_comment.html'
    form_class = forms.CommentsCreateForm
