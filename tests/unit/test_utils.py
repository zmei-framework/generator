from zmei_generator.generator.utils import gen_args


def test_gen_args():
    assert gen_args({'a': 123, 'b': "lala"}) == "a=123, b='lala'"


def test_gen_args_extend():
    assert gen_args({'a': 123, 'b': "lala", '_': 'hoho!'}) == "a=123, b='lala', hoho!"


def test_gen_args_extend_only():
    assert gen_args({'_': 'hoho!'}) == "hoho!"
