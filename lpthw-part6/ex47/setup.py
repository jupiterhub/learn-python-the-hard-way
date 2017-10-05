# setup script is the center of all activity
# in building, distributing and installing modules
try:
    # setuptools, download/build/install packages
    # https://pypi.python.org/pypi/setuptools
    # https://docs.python.org/3/distutils/apiref.html#distutils.core.setup
    from setuptools import setup
except ImportError:
    # building and importing additional module to python
    # https://docs.python.org/3/library/distutils.html
    # setuptools is preferred, and enhanced version
    from disutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Jupiter Tecson',
    'url': ' https://github.com/jupiterhub/learn-python-the-hard-way',
    'download_url': 'https://github.com/jupiterhub/learn-python-the-hard-way',
    'author_email': 'jupiter.adverts@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'], # will look for NAME/__init__.py
    #  for small distro, this can be alternative to listing a package
    # it is expected to be under the root folder
    # 'py_modules': ['mod1', 'pkg.mod2']
    'scripts': [],
    'name': 'ex47'
}

# ** pass the key=value as an argument
# ie. setup(description="", author="") and so on
# ** is also called kwargs
# read more on https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
setup(**config)
