from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='categorical-colour-calendar',
    version='0.0.1',
    description='Highlight dates on monthly calendar(s) from categorical event data',
    py_modules=['cccalendar'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erichards97/categorical-colour-calendar',
    author='Edward Richards',
    author_email='',
    install_requires=[
        'pandas>=1.2.1',
        'matplotlib>=3.3.4'
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.2'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)