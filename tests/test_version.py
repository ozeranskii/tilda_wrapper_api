#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of tilda_wrapper_api.
# https://github.com/ozeranskiy/tilda_wrapper_api

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2019, Sergey Ozeranskiy <sergey.ozeranskiy@gmail.com>

# Project
from tests.base import TestCase
from tilda_wrapper_api import __version__


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        self.assertEqual(__version__, '0.1.0')
