"""
Flask-EasyMDE
-------------
Flask implementation for EasyMDE Markdown Editor
EasyMDE is a fork of abandoned SimpleMDE project which brings new features and fix bugs
"""
from setuptools import setup


setup(
    name='Flask-EasyMDE-dnymxm',
    version='1.4',
    url='https://github.com/dnymxm/flask-easymde/',
    license='BSD',
    author='Maxime Diony',
    author_email='maxime.diony@gmail.com',
    description="Flask implementation for EasyMDE Markdown Editor",
    long_description=__doc__,
    py_modules=['flask_easymde', 'tests'],
    python_requires=">= 3.6",
    zip_safe=False,
    include_package_data=True,
    packages=['flask_easymde'],
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
