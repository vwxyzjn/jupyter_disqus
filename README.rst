.. title:: Jupyter_Disqus Package

Jupyter_Disqus Package
=======================

.. image:: https://travis-ci.org/vwxyzjn/jupyter_disqus.svg?branch=master
    :target: https://travis-ci.org/vwxyzjn/jupyter_disqus

.. image:: https://codecov.io/gh/computationalmodelling/python-package-template/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/computationalmodelling/python-package-template

.. image:: https://badge.fury.io/py/jupyter-disqus.svg
    :target: https://badge.fury.io/py/jupyter-disqus


You may use this package to inject and display `Disqus <https://disqus.com/>`_ in your jupyter notebook. 

Demo
=======================

.. image:: demo.gif
    :target: demo.gif


Installation
=====================

::

  $ pip install jupyter_disqus


Usage
==========

.. code-block:: python

    from jupyter_disqus import inject
    # make sure to run this in a cell of your jupyter notebook
    inject(
        page_url="https://costahuang.me",
        page_identifier="SC2AI/",
        site_shortname="costahuang"
    )


Documentation `on Readthedocs <http://python-package-template.readthedocs.io/>`__.

Setting up external services:

- Travis (for running the tests): log in to https://travis-ci.org/ with your
  Github account and flip the switch for the repository.
- The tests running on Travis will automatically set up the project on
  https://codecov.io/
- Readthedocs: log in to https://readthedocs.org/ with your Github account, and
  add the repository.

Authors: Costa Huang
