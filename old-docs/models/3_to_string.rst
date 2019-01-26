To string
##############

"To string" is a way to represent model when it’s printed or converted to a string. 
It’s often used to display models.

Field
==========

The easiest way to convert to string is to add a "=" modifier to the field::

    #cat
    -------
    =name


The resulting code is::

    class Cat(model.Model):
        name = models.CharField(null=True, blank=True, max_length=100, default='')

        def __str__(self):
            return str(self.name) or "Cat {}".format(self.id)

Expression
===============

Another option is to use an expression. The syntax is as follows::

    ="some expression here"

An expression is just a string template with a "me" variable (python .format() function) ::

    #project_note
    --------------------
    ="{me.project} -> {me.date:%d.%m.%Y}: #{me.id}"

    project: one(#project -> notes)

    date: date
    text: longtext
