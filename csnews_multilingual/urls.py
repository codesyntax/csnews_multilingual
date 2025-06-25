from django.urls import re_path
from csnews_multilingual.feeds import LatestNews
from django.utils.translation import gettext_lazy as _

from csnews_multilingual import views

urlpatterns = [
    re_path(r'^$', views.index, name='csnews_index'),
    re_path(_(r'^tag/(?P<tag_slug>[\-\d\w]+)$'), views.tag_index, name='csnews_tag'),
    re_path(_(r'^feed$'), LatestNews(), name='csnews_feed'),
    re_path(_(r'^archive$'), views.archive, name='csnews_archive'),
    re_path(_(r'^(?P<article_slug>[\-\d\w]+)$'), views.article_index, name='csnews_article'),
]