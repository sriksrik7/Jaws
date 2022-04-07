from setuptools import setup, find_packages

setup(
    name='backend',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'geopy',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
