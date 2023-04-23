from setuptools import setup, find_packages

setup(
    name='kaggle_util',
    version='0.1.0',
    author='Satya Pati',
    author_email='iamsatyapati@gmail.com',
    description='A utility for working with Kaggle competitions.',
    url='https://github.com/neural-navigator/kaggle_utility',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kaggle_util=kaggle_util:main'
        ]
    },
    install_requires=[
        'kaggle>=1.5.12'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
