from setuptools import setup, find_packages
import os

version = '2.0.1'

setup(name='plonetheme.bootstrap',
      version=version,
      description="bootstrap css integration",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='plone theme twitterbootstrap',
      author='Nathan van Gheem, Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='https://github.com/collective/plonetheme.bootstrap',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          'plone.browserlayer',
          'collective.js.bootstrap>=3.0',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing[robot]>=4.2.2',
              'plone.app.robotframework',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """
      )
