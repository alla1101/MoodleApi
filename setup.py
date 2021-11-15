from setuptools import setup,find_packages

setup(
    name='My Script',
    version='0.1.0',
    py_modules=['yourscript','myscript','mainscript'],
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'allascript = yourscript:cli',
            'aliscript = myscript:cli',
            'mainscript = mainscript:main'
        ],
    },
)