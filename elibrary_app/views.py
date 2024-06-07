from django.shortcuts import render
from .forms import AddBookForm
from .models import Catalog

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView

from blog.models import Post


class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    fields = ('name', 'content')
    template_name = "post.html"


def home(request):
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
    books = Catalog.objects.all()
    add_book_form = AddBookForm()

    return render(request, 'home.html', {
        "add_book_form": add_book_form,
        "books": books
    })