from modeltranslation.translator import translator, TranslationOptions
from .models import Article, Tag, PhotoExtended

class ArticleTranslationOptions(TranslationOptions):
    fields = ()

class TagTranslationOptions(TranslationOptions):
    fields = ()

class PhotoExtendedTranslationOptions(TranslationOptions):
    fields = ()

translator.register(Article, ArticleTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(PhotoExtended, PhotoExtendedTranslationOptions)