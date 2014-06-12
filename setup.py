#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


__author__ = "Christian Felder <webmaster@bsm-felder.de>"
__date__ = "2014-06-12"
__version__ = "0.0.1"
__copyright__ = """Copyright 2014, Christian Felder

This file is part of renameFile, a script to rename files with consecutive
numbers. Visit https://code.bsm-felder.de for the latest version.

renameFile is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

renameFile is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with renameFile. If not, see <http://www.gnu.org/licenses/>.

"""

setup(name="renameFile",
      version=__version__,
      description="renameFile, renaming files with consecutive numbers.",
      author="Christian Felder",
      author_email="webmaster@bsm-felder.de",
      license="GNU General Public License",
      url="http://code.bsm-felder.de",
      package_dir={'': "src"},
      scripts=["src/renameFile"]
      )
