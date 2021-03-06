from django.db import models

status_choices = [("active", "Активно"), ("blocked", "Заблокировано")]
# Create your models here.

class Guestbook(models.Model):
    author = models.CharField(max_length=150, null=False, blank=False,  verbose_name='Автор')
    email = models.EmailField(max_length=150, null=False, blank=False, verbose_name='Почта ')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст ')
    time_of_creation = models.DateTimeField(auto_now_add=True)
    time_of_update = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=150, null=False, blank=False, choices=status_choices, default="active")

    class Meta:
        db_table = 'Guestbook'
        verbose_name = 'Гостевая книга'
        verbose_name_plural = 'Гостевая книги'

    def __str__(self):
        return f'{self.id}. {self.author}'
