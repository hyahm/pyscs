from setuptools import setup, find_packages
import io
import os


here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = ""
    
setup(
    name="pyscs",
    packages=find_packages(),
    version='0.0.10',
    description="support scs >=2.5.1 client lib for python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="cander",
    author_email='cander_liubiao@126.com',
    url="https://github.com/hyahm/pyscs",
    install_requires=[
        'requests',
    ]
)