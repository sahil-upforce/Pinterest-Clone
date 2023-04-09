from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_('Category'), max_length=150, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.name = self.name.title()
        return super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
