from setuptools import setup


setup(
    name='pa11y_runner',
    version='0.1',
    py_modules=['pa11y_runner'],
    install_requires=[
        'Click',
        'termcolor',
    ],
    entry_points='''
        [console_scripts]
        pa11y_runner=pa11y_runner:run
    ''',
)
