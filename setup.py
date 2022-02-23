from setuptools import setup



setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line Task-app written in Python',
    author='Mohammed Taher',
    install_requires=['tabulate'],
    entry_points={
        'console_scripts': [
            'taskaty=taskaty:main',
        ],
    },
)
