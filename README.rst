Introduction
============

plonetheme.bootstrap integrates Twitter Bootstrap CSS/JS framework
into Plone. You can checkout the framework at http://getbootstrap.com/

It overrides some templates and uses javascript to transform
some markup in order for it to work correctly.

It's not perfect, but it's close.

.. image:: https://api.travis-ci.org/collective/plonetheme.bootstrap.png?branch=master
    :target: http://travis-ci.org/collective/plonetheme.bootstrap

Dependencies
==============

Latest Twitter Bootstrap requires jQuery 1.11, you can install
it in Plone pinning plone.app.jquery in your buildout to version 1.11.2.
You will also need to pin plone.app.jquerytools to version
1.7.0 to guarantee compatibility. Twitter Boostrap itself is provided as
browser resources by the addon `collective.js.bootstrap`_ so you need to pin
it aswell.::

 [versions]
 ...
 plone.app.jquery = 1.11.2
 plone.app.jquerytools = 1.7.0
 collective.js.bootstrap = 3.3.5
 ...



Documentation
===============

This product is based in Twitter Bootstrap version 3. The product will reuse
`collective.js.bootstrap`_ to get those CSS and JS files.

The basic HTML markup is a mix of `plonetheme.sunburst`_ and Twitter Bootstrap
and it uses the same approach of constructing the columns as Sunburst Theme:
a simple view that returns the classes needed to have the correct column widths.

If you want to change those widths, just override the view following the common
Plone overriding patterns.

This product is intended to be used in two scenarios:

 - As a theme from Plone
 - As a base theme to build Plone themes for your site following 'old practices'

Some designers prefer to work following the old best-practices instead of using
the Diazo-way-of-theming, this product is for them. You can create a theme package
(check `templer skeleton generator`_), and base your theme on this one.

If you have any problem using this product or find any bug, please report it
using the `GitHub issue tracker`_.

Upgrade
=========

To upgrade from version 1.0a1, just go to the add-on controlpanel and click
on upgrade. Old skin paths and javascripts will be disabled and new ones imported



Authors
=========

- Nathan van Gheem, initial author
- Mikel Larreategi, update to Twitter Bootstrap 2.3.x, current mantainer



.. _`plonetheme.sunburst`: http://pypi.python.org/pypi/plonetheme.sunburst
.. _`templer skeleton generator`: http://templer-manual.readthedocs.org/en/latest/
.. _`GitHub issue tracker`: https://github.com/collective/plonetheme.bootstrap/issues
.. _`collective.js.bootstrap`: https://pypi.python.org/pypi/collective.js.bootstrap
