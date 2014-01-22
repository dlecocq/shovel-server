#! /usr/bin/env python
import sys

try:
    from setuptools import setup
    extra = {
        'install_requires': ['argparse']
    }
    if sys.version_info >= (3,):
        extra['use_2to3'] = True
except ImportError:
    from distutils.core import setup
    extra = {
        'dependencies': ['argparse']
    }

setup(name               = 'shovel-server',
    version              = '0.1.0',
    description          = 'Shovel Tasks in Server Form',
    url                  = 'http://github.com/seomoz/shovel-server',
    author               = 'Dan Lecocq',
    author_email         = 'dan@moz.com',
    license              = "MIT License",
    keywords             = 'tasks, shovel, rake, server',
    packages             = ['shovel.server'],
    package_dir          = {'shovel.server': 'shovel'},
    package_data         = {'shovel.server': [
        'templates/*.tpl', 'static/css/*']},
    include_package_data = True,
    scripts              = ['bin/shovel-server'],
    classifiers          = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    **extra
)
