from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-taijiang',
    version=version,
    description="CKAN extension for the Taijiang Research Database",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Sol Lee',
    author_email='u103133.u103135@gmail.com',
    url='',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.taijiang'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.taijiang.plugin:PluginClass
	taijiang_datasets = ckanext.taijiang.plugin:TaijiangDatasets
    ''',
)
