import pytest


@pytest.mark.zmei('sample', """

#car
-------
nr
mark
model
weight: int
crashed: bool(true)
painted: bool

""")
@pytest.mark.zmei_before('migrate')
def test_simple():
    from sample.models import Car

    bmw = Car(mark='BMW')
    bmw.save()

    assert Car.objects.count() > 0
    assert bmw.id is not None

    assert Car.objects.get(pk=1).mark == 'BMW'

    # check bool default values
    assert bmw.crashed
    assert not bmw.painted


@pytest.mark.zmei('sample', """

#dog
-------
sound:= 'Bark!'

""")
@pytest.mark.zmei_before('migrate')
def test_expression():
    from sample.models import Dog

    dog = Dog()

    assert dog.sound == 'Bark!'
