import os

import pytest


@pytest.mark.django_gen('poly', """

#animal
------------
name

#animal->cat
-------------
tail_length: int

""")
@pytest.mark.django_gen_before('migrate')
def test_model_parent():
    from poly.models import Cat, Animal

    assert issubclass(Cat, Animal)


@pytest.mark.django_gen('poly', """

#animal
------------
name

#animal~>cat
-------------
tail_length: int

""")
@pytest.mark.django_gen_before('migrate')
def test_model_parent_with_prefix():
    from poly.models import AnimalCat, Animal

    assert issubclass(AnimalCat, Animal)
