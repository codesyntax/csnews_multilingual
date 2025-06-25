from django.contrib import admin
from csnews_multilingual.models import Article, Tag, PhotoExtended
from csnews_multilingual.forms import PhotoAdminExtendedForm
from django.conf import settings
from tinymce.widgets import TinyMCE
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Photo
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


def show_entry_thumbnail(item):
    if item.image:
        return item.image.admin_thumbnail()
    else:
        return None

show_entry_thumbnail.short_description = 'Argazkia'
show_entry_thumbnail.allow_tags = True


class TagAdmin(TranslationAdmin):
    list_display = ('name', 'added')
    list_display_links = ('name',)
    ordering = ('-added',)
    search_fields = ['name', ]


class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'published', 'is_public', show_entry_thumbnail)
    list_display_links = ('title',)
    ordering = ('-id',)
    search_fields = ['title', 'summary',]
    filter_horizontal = ('tags',)
    photologue_image_fields = ('image',)

    fieldsets = (
        (_("Language dependent"), {
            'fields': ('title', 'summary', 'body', 'tags'),
        }),
        (_("Common"), {
            'fields': ('published', 'image', 'is_public'),
        }),
    )


class TinyMCEArticleAdmin(ArticleAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ('body', 'summary'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs=settings.TINYMCE_DEFAULT_CONFIG,
            ))
        return super(TinyMCEArticleAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)


class PhotoExtendedInline(TranslationStackedInline):
    model = PhotoExtended
    can_delete = False


class PhotoAdmin(PhotoAdminDefault):
    form = PhotoAdminExtendedForm
    inlines = [PhotoExtendedInline, ]


admin.site.register(Article, TinyMCEArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)