from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_blank():
    app = _("""
    
        [foo]
        lala := 123
    """)

    foo = app.pages['foo']

    lala = foo.page_items['lala']

    assert lala.serialize is False
    assert lala.model_name is None
    assert lala.model_descriptor is None
    assert lala.model_many is None


def test_simple():
    app = _("""
    
        [foo]
        lala := 123 #test
    """)

    foo = app.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.model_name == 'test'
    assert lala.model_descriptor is None
    assert lala.model_many is False


def test_long():
    app = _("""
    
        [foo]
        lala := 123 #test.lala
    """)

    foo = app.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.model_name == 'test.lala'
    assert lala.model_descriptor is None
    assert lala.model_many is False
    assert lala.model_dict is False


def test_long_many():
    app = _("""
    
        [foo]
        lala := 123 #test.lala[]
    """)

    foo = app.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.model_name == 'test.lala'
    assert lala.model_descriptor is None
    assert lala.model_many is True
    assert lala.model_dict is False


def test_long_dict():
    app = _("""
    
        [foo]
        lala := 123 #test.lala{}
    """)

    foo = app.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.model_name == 'test.lala'
    assert lala.model_descriptor is None
    assert lala.model_many is False
    assert lala.model_dict is True



def test_long_dict_descriptor_rest():
    app = _("""
    
        [foo]
        lala := 123 @rest.boo #test.lala{}
    """)

    foo = app.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is True
    assert lala.model_name == 'test.lala'
    assert lala.model_descriptor == 'boo'
    assert lala.model_many is False
    assert lala.model_dict is True

