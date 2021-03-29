from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apps.blog.blog_entry_repository import BlogEntryRepository


class CreateBlogEntryView(generic.View):
    def get(self, request):
        return render(request, 'blog/new.html')


class BlogEntriesView(generic.View):
    __repo = BlogEntryRepository()

    def post(self, request):
        entry = self.__repo.create(
            title=request.POST['title'],
            body=request.POST['body'],
            author=request.POST['author'],
        )

        return HttpResponseRedirect(reverse('blog:entry_detail', args=[entry.id]))

    def get(self, request):
        entries = self.__repo.list()

        return render(request, 'blog/list.html', {'blog_entries': entries})


class BlogEntryView(generic.View):
    __repo = BlogEntryRepository()

    def get(self, request, pk: int):
        entry = self.__repo.find(pk)

        return render(request, 'blog/detail.html', {'entry': entry})


class DeleteBlogEntryView(generic.View):
    __repo = BlogEntryRepository()

    def post(self, request, pk: int):
        self.__repo.delete(pk)

        return HttpResponseRedirect(reverse('blog:entries'))
