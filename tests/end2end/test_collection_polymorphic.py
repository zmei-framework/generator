import os

import pytest


@pytest.mark.zmei('poly', """

#animal
------------
name

#animal->cat
-------------
tail_length: int

""")
@pytest.mark.zmei_before('migrate')
def test_model_parent():
    from poly.models import Cat, Animal

    assert issubclass(Cat, Animal)


@pytest.mark.zmei('poly', """

#animal
------------
name

#animal~>cat
-------------
tail_length: int

""")
@pytest.mark.zmei_before('migrate')
def test_model_parent_with_prefix():
    from poly.models import AnimalCat, Animal

    assert issubclass(AnimalCat, Animal)
