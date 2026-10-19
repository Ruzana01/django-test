from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(default='', verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    #Поле для хранения количества лайков/просмотров
    likes = models.IntegerField(default=0, verbose_name="Количество лайков")

    def __str__(self):
        return self.title