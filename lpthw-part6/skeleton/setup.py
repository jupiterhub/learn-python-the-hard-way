try:
    # setuptools, download/build/install packages
    # https://pypi.python.org/pypi/setuptools
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
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

# what is a double **?
setup(**config)
