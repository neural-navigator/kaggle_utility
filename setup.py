from setuptools import setup

setup(
    name='kaggle_util',
    version='1.0',
    packages=['kaggle_utility'],
    entry_points={
        'console_scripts': [
            'kaggle-util = kaggle_utility.kaggle_util:main'
        ]
    }
)
