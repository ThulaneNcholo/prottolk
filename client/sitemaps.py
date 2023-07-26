from django.contrib import sitemaps
from django.db.models.base import Model
from django.urls import reverse


class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["client:index", "client:about", "client:services", "client:gallery", "client:contact",]

    def location(self, item):
        return reverse(item)
