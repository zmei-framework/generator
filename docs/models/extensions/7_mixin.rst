@mixin
###########

Sometimes it’s required to extend the generated model using custom functions. The most accurate way to do so is to use mixins::

    #page
    -------------
    =*title
    ~slug: slug(title)
    url

    @tree
    @mixin(pages.mixins.PageDeepUrl)


And *pages.mixins.PageDeepUrl* may look like this, for example::

    from django.conf import settings


    class PageDeepUrl(models.Model):

        def get_full_url():
            if not self.parent:
                return self.url

            return '{}/{}'.format(self.parent.get_full_url(), self.url)

        class Meta:
            abstract = True

