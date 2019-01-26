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


@pytest.mark.zmei('poly', """


#data_source
--------------
name

@admin

#data_source_field
---------------------
data_source: one(#data_source -> field_list)
name
type: str(?, choices=string,integer)


#data_source->db_data_source
-------------------
database
server

@admin

#data_source->report_data_source
-------------------
report

@admin


""")
@pytest.mark.zmei_before('migrate')
def test_poly_with_admin():
    pass
