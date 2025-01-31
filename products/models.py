from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='categories/', blank=True)
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='products/', blank=True)
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FFILE_PDF = 3
    FILE_TYPES =(
        (FILE_AUDIO, _('Audio')),
        (FILE_VIDEO, _('Video')),
        (FFILE_PDF, _('Pdf')),
    )
    product = models.ForeignKey('products.Product', verbose_name=_('product'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(_('Type file: '), choices=FILE_TYPES)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title
