
.. role:: done
    :class: done

.. role:: todo
    :class: todo


Roadmap
========================

Zmei generator is the second iteration of generator development.
Previous version was called "Genius" it had slow not that smart parser, no tests and lot of architecture problems.
The current architecture and syntax are mature and battle proven.

* Parser

    * :done:`Pyparsing parser`
    * :done:`Replace pyparsing with cpyparsing`
    * :done:`Write unit tests`
    * :done:`Write integration tests`
    * :done:`Switch to full TDD process`
    * :done:`Replace cpyparsing with ANTLR4 based parser`
    * :done:`Syntax improvements`
    * :done:`Remove deprecated features`
    * :todo:`Other *.col file includes`

* Tooling

    * :done:`ANTLR4 based PyCharm plugin for syntax highlighting`
    * :done:`Zmei Apps development servers`
    * :todo:`Add auto-complete to plugin`
    * :todo:`Add code navigation to plugin``

* Models

    * :done:`Model generator`
    * :done:`Model custom imports`
    * :done:`Calculated fields`
    * :done:`Custom field options and types`
    * :done:`Polymorphic models`
    * :done:`Tree models`
    * :done:`Signal handlers`
    * :todo:`More customisation possibilities`

* Pages

    * :done:`Page generator`
    * :done:`Page custom imports`
    * :done:`Page inheritance`
    * :done:`Improve generated code redability`
    * :done:`CRUD pages`
    * :done:`Page custom code`
    * :done:`Menu`
    * :done:`Authentication`
    * :done:`Error pages (404, 500 etc)`
    * :done:`Global context`

* Admin

    * :done:`Admin generator`
    * :done:`Inlines`
    * :done:`Polymorphic inlines`

* REST framework

    * :done:`REST api generator`
    * :done:`Auth module (basic, token, session)`
    * :done:`Inlines`
    * :done:`Nested inlines`
    * :done:`Multiple serializers on the same model`
    * :todo:`Swagger integration`
    * :todo:`API client generator`
    * :todo:`JWT authentication`

* React

    * :done:`React support prototype`
    * :todo:`React support`
    * :todo:`Streams API (websocket)`
    * :todo:`React native? other mobile technologies?`

* Other

    * :done:`Add celery support`
    * :todo:`RabbitMQ support`
    * :todo:`RabbitMQ advanced patterns`

