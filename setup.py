"""
This module contains the setup script for the 'asyncio-nats-streaming' package.

The setup script defines the package metadata, such as name, version, description, classifiers, etc.
It also specifies the package dependencies and other configuration options.
"""
import ast
import re

from setuptools import setup

# Regular expression pattern to extract the version number from the source code
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('stan/aio/client.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='asyncio-nats-streaming',
    version=version,
    description='NATS Streaming client for Python Asyncio',
    long_description='Asyncio based Python client for NATS Streaming',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    url='https://github.com/nats-io/stan.py',
    author='LiveOpsEngineering',
    author_email='drmargarido@lockwood-publishing.com',
    license='Apache 2 License',
    packages=['stan', 'stan.aio', 'stan.pb'],
    zip_safe=True,
    install_requires=['protobuf>=3.7', 'nats-py>=2.7.0'],
)
