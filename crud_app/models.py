from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title