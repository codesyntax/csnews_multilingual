from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class CSNewsConfig(AppConfig):
    name = 'csnews_multilingual'
    verbose_name = _("News")