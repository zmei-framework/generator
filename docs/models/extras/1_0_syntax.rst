Overview
###########

Extras is a way how to extend model functionality. It alows
to add some special behaviour or even generate another types
of source files, like Admin panel or Restful interfaces for model.

Common syntax
==================

Extra structure is following::

    @extra_name.descriptor optional_extra_body

Descriptor is optional. It is used in some extras to clarify name or unique id
of extra, if several extras of same name is used in one place.

Extra body may be anything, surrounded in pair of braces. Braces may be of following types:

- <@  @>
- <<  >>
- {{  }}
- {   }
- (   )

Syntactically there is no difference which braces to use, but common rule is that brace type
should not apper inside braces, through there is no way to escape them. Also right choice
of braces makes .col file code more readable.

Examples
============

"{ }" braces on a page's menu extra::

    [base]
    @menu.left {
        index => "Home": page(index)
        docs => "Documentation": url('/docs/generator/index.html')
    }
    @menu.right {
        dashboard => Dashboard: page(dashboard)
    }

"( )" braces on a model::

    #token
    ----------
    name
    user: one(cratis_profile.User)

    @mixin(rest_framework.authtoken.models.Token)

"<< >>" braces on m2m event handler::

    #request_file
    -----------------
    request: one(#request -> files)
    user: one(cratis_profile.User)
    =name: text(255)
    body: longtext

    @m2m_changed<<
        print(args.instance, args.action)
    >>


