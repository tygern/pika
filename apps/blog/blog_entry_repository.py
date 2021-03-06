from django.db import models
from django.db.models.functions import Now

from apps.blog.blog_entry import BlogEntry


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class BlogEntryRecord(models.Model):
    objects = NotDeletedManager()

    db_table = 'blog_entries'

    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class BlogEntryRepository:
    __manager = BlogEntryRecord.objects

    def create(self, title: str, body: str, author: str) -> BlogEntry:
        record = self.__manager.create(title=title, body=body, author=author)

        return self.__entry_from_record(record)

    def list(self) -> list[BlogEntry]:
        records = self.__manager.all()

        return list(map(self.__entry_from_record, records))

    def find(self, id: int) -> BlogEntry:
        return self.__manager.get(pk=id)

    def delete(self, id: int) -> None:
        self.__manager.filter(pk=id).update(deleted_at=Now())

    @staticmethod
    def __entry_from_record(record) -> BlogEntry:
        return BlogEntry(
            id=record.id,
            title=record.title,
            body=record.body,
            author=record.author,
            created_at=record.created_at,
            updated_at=record.updated_at,
        )
