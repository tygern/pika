from django.urls import path

from apps.blog.blog_entry_views import BlogEntriesView, BlogEntryView, CreateBlogEntryView, DeleteBlogEntryView

app_name = 'blog'
urlpatterns = [
    path('', BlogEntriesView.as_view(), name='entries'),
    path('<int:pk>', BlogEntryView.as_view(), name='entry_detail'),
    path('<int:pk>/delete', DeleteBlogEntryView.as_view(), name='delete_entry'),
    path('new', CreateBlogEntryView.as_view(), name='new_entry'),
]
