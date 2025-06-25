from modeltranslation.translator import translator, TranslationOptions
from .models import Article, Tag, PhotoExtended

class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'body', 'slug',)

class TagTranslationOptions(TranslationOptions):
    fields = ('name', 'slug',)

class PhotoExtendedTranslationOptions(TranslationOptions):
    fields = ('caption',)

translator.register(Article, ArticleTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(PhotoExtended, PhotoExtendedTranslationOptions)