from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from mainapp.models import Course, Event


class Site:
    domain = 'crm.f-academy.ru'


class MainSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['/']

    def location(self, item):
        return item

    def get_urls(self, site=None, protocol=None, **kwargs):
        site = Site()
        return super(MainSitemap, self).get_urls(site=site, protocol='https', **kwargs)


class CourseSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Course.objects.filter(is_active=True)

    def location(self, obj):
        return f'/education/{obj.slug}'

    def get_urls(self, site=None, protocol=None, **kwargs):
        site = Site()
        return super(CourseSitemap, self).get_urls(site=site, protocol='https', **kwargs)


class EventSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Event.objects.all()

    def location(self, obj):
        return f'/events/{obj.slug}'

    def get_urls(self, site=None, protocol=None, **kwargs):
        site = Site()
        return super(EventSitemap, self).get_urls(site=site, protocol='https', **kwargs)


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['education', 'events', 'contacts', 'about', 'reviews', 'career', 'news']

    def location(self, item):
        return f'/{item}'

    def get_urls(self, site=None, protocol=None, **kwargs):
        site = Site()
        return super(StaticViewSitemap, self).get_urls(site=site, protocol='https', **kwargs)
