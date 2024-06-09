from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponseNotFound
from books.models import Book


class BookListView(View):

    def get(self, request, *args, **kwargs):
        book_list = Book.objects.all()
        return render(request, 'base.html', {'book_list': book_list})
