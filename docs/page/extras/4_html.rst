
@html and @markdown
#####################

@html
========

Html allows to insert blocks of html content into the page template::

    [boo]
    @html {
        <h1>test</h1>
    }

Also you can specify in which template block to insert the html piece by
adding a descriptor to annotation::

    [boo]
    @html.foo {
        <h1>test</h1>
    }


@markdown
===========

Markdown is very similar to @html, except it accepts markdown and convert it to html::

    [boo]
    @markdown {
        # test
    }

Same as with @html can specify in which template block to insert the html piece by
adding a descriptor to annotation::

    [boo]
    @markdown.foo {
        # test
    }
