from django.db import models
from django.utils.translation import gettext_lazy as _
from photologue.models import Photo
from django.urls import reverse
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=300)
    slug = models.CharField(_("Slug"), max_length=200, db_index=True, blank=True)
    added = models.DateField(_("Added"), auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ("-added",)

    def __str__(self):
        return self.name


class Article(models.Model):
    published = models.DateTimeField(_("Published"))
    image = models.ForeignKey(Photo, null=True, blank=True, related_name="news_images", on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    is_public = models.BooleanField(_("Is public"), default=True)

    added = models.DateField(_("Added"), auto_now_add=True)
    modified = models.DateField(_("Modified"), auto_now=True)

    title = models.CharField(_("Title"), max_length=200)
    summary = models.TextField(_("Summary"), blank=True)
    body = models.TextField(_("Body"))
    slug = models.CharField(_("Slug"), max_length=200, db_index=True, blank=True)

    def get_title(self):
        return self.title

    def get_absolute_url(self):
        return reverse("csnews_article", kwargs={"article_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-published",)
        get_latest_by = "published"

    def __str__(self):
        return self.title


class PhotoExtended(models.Model):
    photo = models.OneToOneField(Photo, related_name="extended", on_delete=models.CASCADE)

    caption = models.TextField(_("caption"), blank=True)

    class Meta:
        verbose_name = _("Multilingual Caption")
        verbose_name_plural = _("Multilingual Captions")

    def __str__(self):
        return self.photo.title