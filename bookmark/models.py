from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True,
    )
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='bookmarks', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'
