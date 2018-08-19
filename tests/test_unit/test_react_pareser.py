from cratis_generator.extras.page.react import react_extra_parser


def test_basic_usage():
    str = """
use([@material-ui/core] @material-ui/core: Button)

<h1>Hello, world!

    <Button variant="contained" color="primary">
        Hello World
    </Button>
</h1>
    """

    res = react_extra_parser.parseString(str)

    assert res.use[0].package_name == '@material-ui/core'
    assert res.use[0].import_from == '@material-ui/core'
    assert res.use[0].components == ['Button']

    assert 'Hello World' in res.source
