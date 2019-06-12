from __future__ import print_function
from setuptools import setup, find_packages
import sys
setup(
name="aihub",
version="0.0.6.1.5",
author="AIHUB",
author_email="ifeel4fun@gmail.com",
description="A Python library for AIHUB.",
license="MIT",
url="https://www.aihub.com.tw/",
packages=['aihub'],
classifiers=[
"Environment :: Web Environment",
'Intended Audience :: Developers',
'License :: OSI Approved :: MIT License',
'Operating System :: MacOS',
'Operating System :: Microsoft',
'Operating System :: POSIX',
'Operating System :: Unix',
"Topic :: Internet",
"Topic :: Software Development :: Libraries :: Python Modules",
'Programming Language :: Python :: 2.6',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
'Programming Language :: Python :: 3.6',
'Programming Language :: Python :: 3.7'
],
zip_safe=True,
install_requires=[
   'requests',
   'six',
   'urllib3'
]
)