from setuptools import setup, find_packages

setup(
    name = 'p3d3',
    version = '0.0.3',
    author = 'Cedric Canovas',
    author_email = 'dev@canovas.me',
    keywords = '',
    packages = ['p3d3'],
    include_package_data=True,
    package_dir={'p3d3':'src'},
    install_requires=['ipython', 'pandas', 'numpy'],
    description = '',
    long_description = 'See https://github.com/cedricfr/p3d3/blob/master/README.md for details.',
    license = 'Apache License v2.0',
    url = 'https://github.com/cedricfr/p3d3',
    test_suite='test',
)
