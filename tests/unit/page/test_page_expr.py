from textwrap import dedent

from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_blank():
    cs = _("""
    
        [foo]
        lala := 123
    """)

    foo = cs.pages['foo']

    lala = foo.page_items['lala']

    assert lala.serialize is False
    assert lala.collection_name is None
    assert lala.collection_descriptor is None
    assert lala.collection_many is None


def test_simple():
    cs = _("""
    
        [foo]
        lala := 123 #test
    """)

    foo = cs.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.collection_name == 'test'
    assert lala.collection_descriptor is None
    assert lala.collection_many is False


def test_long():
    cs = _("""
    
        [foo]
        lala := 123 #test.lala
    """)

    foo = cs.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.collection_name == 'test.lala'
    assert lala.collection_descriptor is None
    assert lala.collection_many is False
    assert lala.collection_dict is False


def test_long_many():
    cs = _("""
    
        [foo]
        lala := 123 #test.lala[]
    """)

    foo = cs.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.collection_name == 'test.lala'
    assert lala.collection_descriptor is None
    assert lala.collection_many is True
    assert lala.collection_dict is False


def test_long_dict():
    cs = _("""
    
        [foo]
        lala := 123 #test.lala{}
    """)

    foo = cs.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is False
    assert lala.collection_name == 'test.lala'
    assert lala.collection_descriptor is None
    assert lala.collection_many is False
    assert lala.collection_dict is True



def test_long_dict_descriptor_rest():
    cs = _("""
    
        [foo]
        lala := 123 @rest.boo #test.lala{}
    """)

    foo = cs.pages['foo']

    lala = foo.page_items['lala']
    assert lala.serialize is True
    assert lala.collection_name == 'test.lala'
    assert lala.collection_descriptor == 'boo'
    assert lala.collection_many is False
    assert lala.collection_dict is True

