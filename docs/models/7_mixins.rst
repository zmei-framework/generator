Mixins
###########

Sometimes it's need to extend generated model with custom functionality.
Most accurate way to do so is to use mixins::

    #page
    -------------
    =*$title
    ~$slug: slug(title)
    $url

    ...

    @mixin(pages.mixins.PageDeepUrl)

And *pages.mixins.PageDeepUrl* may look like this, for example::

    from django.conf import settings


    class PageDeepUrl(models.Model):

        ..

        def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
            for lang, name in settings.LANGUAGES:
                setattr(self, 'url_' + lang, self.get_url(lang))

                if not getattr(self, 'slug_' + lang):
                    setattr(self, 'slug_' + lang, self.slug)

            super().save(force_insert, force_update, using, update_fields)

            for page in self.children.all():
                page.save()

        class Meta:
            abstract = True

Generated code is just class added to model base classes::

    class Page(PageDeepUrl, models.Model):
        ...

        title = models.CharField(null=True, blank=False, max_length=100)
        slug = models.SlugField(blank=True, max_length=100, default='')
        url = models.CharField(null=True, blank=True, max_length=100, default='')

        ...

