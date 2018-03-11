To string
##############

"To string" is a way to represent model when it's printed or converted to string. It's
often used to display models.

Field
==========

Easiest way to add to string conversion is add "=" modifier to the field::

    #cat
    -------
    =name


Resulting code is::

    class Cat(model.Model):
        name = models.CharField(null=True, blank=True, max_length=100, default='')

        def __str__(self):
            return str(self.name) or "Cat {}".format(self.id)

Expression
===============

Another option is to use expression. Syntax is following::

    ="some expression here"

Expression is just a string template with "me" variable (python .format() function) ::

    #project_note
    --------------------
    ="{me.project} -> {me.date:%d.%m.%Y}: #{me.id}"

    project: one(#project -> notes)

    date: date
    text: longtext
