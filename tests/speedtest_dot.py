# encoding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Kyle Lahnakoski (kyle@lahnakoski.com)
#

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import cProfile
import pstats

from mo_testing.fuzzytestcase import FuzzyTestCase
from mo_threads import profiles

from mo_dots import Data, wrap


class SpeedTestDot(FuzzyTestCase):

    def test_simple_access(self):
        """
        THIS WILL WRITE A STATS FILE TO THE PROJECT DIRECTORY
        """
        x = wrap({"a": {"b": 42}})

        cprofiler = cProfile.Profile()
        cprofiler.enable()
        for i in range(1000 * 1000):
            y = x.a
        cprofiler.disable()

        profiles.write(Data(filename="test_dot_speed.tab"), [pstats.Stats(cprofiler)])