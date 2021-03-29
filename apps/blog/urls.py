from django.urls import path

from apps.blog.blog_view import BlogEntriesView, BlogEntryView, CreateBlogEntryView

app_name = 'blog'
urlpatterns = [
    path('', BlogEntriesView.as_view(), name='entries'),
    path('<int:pk>', BlogEntryView.as_view(), name='entry_detail'),
    path('new', CreateBlogEntryView.as_view(), name='new_entry'),
]
