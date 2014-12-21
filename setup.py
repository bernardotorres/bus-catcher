import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bus-catcher',
    version='0.1',
    packages=['buslinesscrapper'],
    include_package_data=True,
    license='GPL v2.0',
    description='Displays Florianopolis bus lines timetables as stem-and-leaf plot',
    long_description=README,
    url='https://github.com/bernardotorres/bus-catcher',
    author='Bernardo Torres',
    author_email='bernardo@torresautomacao.com.br',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
      'Scrapy==0.24.4',
      'Twisted==14.0.2',
      'cffi==0.8.6',
      'cryptography==0.7',
      'cssselect==0.9.1',
      'enum34==1.0.4',
      'lxml==3.4.1',
      'pyOpenSSL==0.14',
      'pyasn1==0.1.7',
      'pycparser==2.10',
      'queuelib==1.2.2',
      'six==1.8.0',
      'w3lib==1.10.0',
      'wsgiref==0.1.2',
      'zope.interface==4.1.1',
    ],
)
