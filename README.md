# Zmei code generator

[![codecov](https://codecov.io/gh/zmei-framework/generator/branch/master/graph/badge.svg)](https://codecov.io/gh/zmei-framework/generator)
[![Build Status](https://travis-ci.org/zmei-framework/generator.svg?branch=master)](https://travis-ci.org/zmei-framework/generator)


Zmei generator is started as simple scaffolding tool for Django. Now it is powerfull
code generator that automate routine work and gently integrates generated sources into your custom code.

Keep it [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)!

## Features

- Quick create configured Django project
- Compact dsl for generating Django-views and models
- Pycharm plugin for syntax highlighting
- Automatic django-admin generation including complex ones: polymorphic, inlines, translatable
- Powerful CRUD generator
- React application generator (TODO: not documented) + channels websocket integration
- Flutter application generator (TODO: not documented)
- Automatic generation of REST endpoints
- Flexible plugin system

## Installation 

Generator is written in python. Install with pip python packaging tool (preferably in virtual environment):

`pip install zmei-cli`
 
## Quick start

Create file "main.col" with page declaration:

    [index: /]
    @markdown {
        # Hello, world!
    }
 
And run zmei command:
 
    zmei gen up
    
In less than a minute you will get all dependency installed and django application
with hello world page on http://127.0.0.1:8000/

## Next steps

See [documentation](https://zmei-framework.com/generator/).

Read tests [unit](https://github.com/zmei-framework/generator/tree/master/tests/unit),
[en2end](https://github.com/zmei-framework/generator/tree/master/tests/end2end).


## Code sample

    @theme(bluma)
    
    [base]
    @menu.navbar (
        "Home": page(index)
        "Another": page(another)
    )
    
    [base->index: /]
    @markdown {
        # This is cats!
    }
    @crud.cats(#cat
        list: tabular
    
        detail(
    
            lala := 123
    
            @markdown {
                # test
            }
    
            @@
    
            @crud.comments(#cat_comment{cat_id=url.cats_pk}
                fields: text
                skip: edit, detail, delete
            )
    
        )
    
        create(
            foo := "This is foo"
        )
    )
    @crud.cars(#car
    
        detail(
            @markdown {
                # carrrr
            }
        )
    )
    
    [base->another: /another]
    
    #cat
    -------
    =name
    age: int
    
    
    #car
    -------
    =model
    year: int
    color: str(?, choices=green,red,blue)
    
    
    #cat_comment
    ----------
    date: create_time
    cat: one(!#cat)
    text: text
    
## Contributing

Contributing guide will be here soon... stay tuned!

## Authors

### Conributors

- Alex Rudakov @ribozz (maintainer)
- ... your name here?

### Thanks to

- github, travis-ci.com and codecov.io for free great services for Open Source projects!

## LEGAL NOTICE

Source code is distributed under GNU General Public License v3.0 licence. Full licence text is available in LICENSE file.

In-short about GPLv3:
- All software that use Zmei-generator as it's part **MUST** be open-sourced as well: plugins, other generators
 based on it, etc.
- You **CAN NOT** take Zmei-generator and sell it as a paid service without open-sourcing it
- But, you **CAN** use Zmei generator as a tool to write any software including private closed source software
 

Software is free for non-commercial use. For commercial use ask for dual-licensing options. 
