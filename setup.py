from setuptools import setup
setup(
    name = 'backend-challenge',
    version = '0.1.0',
    packages = ['msr'],
    entry_points = {
        'console_scripts': [
            'msr = msr.__main__:main'
        ]
    })