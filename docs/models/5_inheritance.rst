Inheritance
################

Models can extend each other::

    #animal
    -------------
    weight

    #animal->cat
    -------------
    name
    tail_len: int


Generated code will be::

    class Animal(PolymorphicModel):
        """
        Animal
        """

        weight = models.CharField(null=True, blank=True,
                                  max_length=100, default='')

        ...


    class Cat(Animal):
        """
        Cat
        """

        name = models.CharField(null=True, blank=True, max_length=100, default='')
        tail_len = models.IntegerField(null=True, blank=True)

        ...

Name prefix
------------------

It's also handy sometimes to add parent model's name as a prefix for current model, then
you can use "~>" operator instead of "->"::

    #block
    ----------
    page: one(#page -> blocks)


    #block~>animated_hero
    ----------
    $content: longtext


    #block~>blog_last
    ----------


    #block~>subpages
    ----------

Generated code will be (note "Block" prefix on every model)::


    class Block(PolymorphicModel):
        """
        Block
        """

        page = models.ForeignKey(
            "Page", null=True, blank=True, related_name='blocks', on_delete=models.CASCADE)
        ...


    class BlockAnimatedHero(Block):
        """
        BlockAnimatedHero
        """

        content = models.TextField(null=True, blank=True, default='')
        ...


    class BlockBlogLast(Block):
        ...


    class BlockSubpages(Block):
        ...


Usage in admin an REST
-------------------------

.. note::

    Almost every piece of the Generator functionality knows how to work with polymorphic models. It just works.