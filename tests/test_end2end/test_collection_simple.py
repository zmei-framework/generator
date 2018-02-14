import os

import pytest


@pytest.mark.django_gen('sample', """

#car
-------
nr
mark
model
weight: int
crashed: bool(true)
painted: bool

""")
@pytest.mark.django_gen_before('migrate')
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


@pytest.mark.django_gen('sample', """

#dog
-------
sound: << 'Bark!';

""")
@pytest.mark.django_gen_before('migrate')
def test_expression():
    from sample.models import Dog

    dog = Dog()

    assert dog.sound == 'Bark!'
