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
    'description': 'My Project',
    'author': 'Jupiter Tecson',
    'url': ' URL to get it at.',
    'download_url': ' Where to download it.',
    'author_email': 'jupiter.adverts@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'], # will look for NAME/__init__.py
    #  for small distro, this can be alternative to listing a package
    # it is expected to be under the root folder
    # 'py_modules': ['mod1', 'pkg.mod2']
    'scripts': [],
    'name': 'projectname'
}

# ** pass the key=value as an argument
# ie. setup(description="", author="") and so on
# ** is also called kwargs
# read more on https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
setup(**config)
