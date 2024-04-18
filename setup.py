from setuptools import find_packages, setup

setup(
    name='harvard_src',
    packages=find_packages(), package_data={
    '': ['*.ini','*.json','*.xml']
    },
    version='0.1.0',
    description='Search Engine',
    author='harvard',
    license='',
)
