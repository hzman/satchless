#! /usr/bin/env python
from setuptools import setup, find_packages

# dynamic retrive version number from stachless.VERSION
version_tuple = __import__('satchless').VERSION
version = '.'.join([str(v) for v in version_tuple])

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

PACKAGE_DATA = {
    '': [
        'locale/**/*.mo',
        'templates/*.*',
        'templates/**/*.*',
    ],
}

REQUIREMENTS = [
    'django-mptt >= 0.4.2',
]

setup(name='satchless',
      author='Mirumee Software',
      author_email='hello@mirumee.com',
      description='An e-commerence framework for Django',
      version = version,
      url = 'http://satchless.com/',
      packages = find_packages(exclude=['doc*', 'examples*', 'tests*',
                                        'website*']),
      package_data=PACKAGE_DATA,
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      platforms=['any'],
      zip_safe=False)
