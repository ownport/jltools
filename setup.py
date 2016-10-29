from setuptools import setup

from jltools import __title__
from jltools import __version__

setup(
    name=__title__,
    version=__version__,
    py_modules=['jltools'],
    entry_points='''
        [console_scripts]
        jltools=jltools.main:cli
    ''',
)
