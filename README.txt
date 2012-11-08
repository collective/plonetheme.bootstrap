Introduction
============

plonetheme.bootstrap integrates the bootstrap css/js framework
into plone. You can checkout the framework at `http://twitter.github.com/bootstrap/`

It overrides some templates and uses javascript to transform
some markup in order for it to work correctly.

It's not perfect, but it's close.

Pin plone.app.jquery to 1.7.1.1 in your buildout as follows::

 [versions]
 ...
 plone.app.jquery = 1.7.1.1
 ...


TODO
----

- better form styles
