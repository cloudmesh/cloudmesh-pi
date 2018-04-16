#!/usr/bin/env python
# ----------------------------------------------------------------------- #
# Copyright 2017, Gregor von Laszewski, Indiana University                #
#                                                                         #
# Licensed under the Apache License, Version 2.0 (the "License"); you may #
# not use this file except in compliance with the License. You may obtain #
# a copy of the License at                                                #
#                                                                         #
# http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                         #
# Unless required by applicable law or agreed to in writing, software     #
# distributed under the License is distributed on an "AS IS" BASIS,       #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.#
# See the License for the specific language governing permissions and     #
# limitations under the License.                                          #
# ------------------------------------------------------------------------#
"""
Cloudmesh PI setup.
"""
import io

from setuptools import find_packages, setup


def readfile(filename):
    """
    Read a file
    :param filename: name of the file
    :return: returns the content of the file as string
    """
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read()


requiers = """
docopt
falcon
""".split("\n")

# dependency_links = ['http://github.com/nicolaiarocci/eve.git@develop']

version = readfile("VERSION").strip()
readme = readfile('README.md')

NAME = "cloudmesh.pi"
DESCRIPTION = "A Library for Raspberry PI IoT and Robots"
AUTHOR = "Gregor von Laszewski"
AUTHOR_EMAIL = "laszewski@gmail.com"
URL = "https://github.com/cloudmesh/cloudmesh.pi"
LONG_DESCRIPTION = readme

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    version=version,
    license="Apache 2.0",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=requiers,
    tests_require=[
        "flake8",
        "coverage",
    ],
    zip_safe=False,
    namespace_packages=['cloudmesh'],
)
