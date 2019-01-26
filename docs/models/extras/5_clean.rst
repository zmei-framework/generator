@clean
###################


With @clean you can add extra validation logic to model. Also can be used to
update model date before save.

Overall validation
====================

If nothing is returned by code, means model is valid. If string is returned,
then it is error for entire model::

    #category
    --------
    name
    title

    @clean {
        if self.name and self.title:
            return "Only one of name or title should be filled!"
    }

Per-field validation
======================

If dictionary is returned, then it is field-specific error::

    #category
    --------
    name
    title

    @clean {
        if self.name.startswith("abc"):
            return {'name': 'You should never start category name with "abc"!'}
    }
