from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, ArticleScope


class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count == 0:
            raise ValidationError('Выберите один главный раздел')
        elif count > 1:
            raise ValidationError('Выбарно более одного главного раздела')
        else:
            return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ScopeInlineFormset
    extra = 1
    verbose_name = 'Тэг'
    verbose_name_plural = 'Тэги'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleScopeInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
