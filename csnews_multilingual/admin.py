from django.contrib import admin
from csnews_multilingual.models import Article
from csnews_multilingual.forms import PhotologueForeignKeyRawIdWidget
from django.conf import settings
from tinymce.widgets import TinyMCE


def show_entry_thumbnail(item):
    if item.image:
        return item.image.admin_thumbnail()
    else:
        return None
    # return item.admin_thumbanail()
show_entry_thumbnail.short_description = 'Argazkia'
show_entry_thumbnail.allow_tags = True


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'published', 'is_public', show_entry_thumbnail)
    list_display_links = ('id', 'title')
    ordering = ('-id',)
    search_fields = ['title', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    photologue_image_fields = ('image',)
    # raw_id_fields = ('image',)
    # form = ArticleAdminForm

class TinyMCEArticleAdmin(ArticleAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('body', 'summary'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={settings.TINYMCE_SETTINGS},
            ))
        return super(TinyMCEArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Article, TinyMCEArticleAdmin)
