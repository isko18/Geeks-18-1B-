from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип сайта'
    )
    is_activ = models.BooleanField(
        default=True,
        verbose_name='ОК'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Найстройки сайта'
        ordering = ['-created_at']