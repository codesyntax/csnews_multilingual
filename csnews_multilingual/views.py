from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.sites.shortcuts import get_current_site
from csnews_multilingual.models import Article, Tag
from django.utils.translation import get_language

ARTICLE_NUMBER_PER_PAGE = 20

def index(request):
    articles = Article.objects.filter(is_public=True)
    return render(request, 'news/articles.html', {'articles': articles})


def tag_index(request, tag_slug):
    obj = get_object_or_404(Tag, slug=tag_slug)
    articles = Article.objects.filter(tags=obj, is_public=True)
    return render(request, 'news/articles.html', {'obj': obj, 'articles': articles})


def article_index(request, article_slug):
    site = get_current_site(request)
    obj = get_object_or_404(Article, slug=article_slug)
    return render(request, 'news/article.html', {'site': site, 'obj': obj})


def archive(request):
    return render(request, 'news/archive.html', {})