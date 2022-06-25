from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    articles = models.ManyToManyField(Article, related_name='tag', blank=True, through='ArticleScope')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['-name']

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='tag')
    is_main = models.BooleanField(verbose_name='Основной', blank=True, default=False)

    class Meta:
        ordering = ['-is_main']
