#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Tue 21 Aug 2012 12:14:43 CEST
#
# Copyright (C) 2011-2013 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Script tests for bob.measure
"""

import os
import unittest
import bob
import pkg_resources

def F(f):
  """Returns the test file on the "data" subdirectory"""
  return pkg_resources.resource_filename(__name__, os.path.join('data', f))

DEV_SCORES = F('dev-4col.txt')
TEST_SCORES = F('test-4col.txt')

DEV_SCORES_5COL = F('dev-5col.txt')
TEST_SCORES_5COL = F('test-5col.txt')

SCORES_4COL_CMC = F('scores-cmc-4col.txt')
SCORES_5COL_CMC = F('scores-cmc-5col.txt')

class MeasureScriptTest(unittest.TestCase):

  def test01_compute_perf(self):

    # sanity checks
    self.assertTrue(os.path.exists(DEV_SCORES))
    self.assertTrue(os.path.exists(TEST_SCORES))

    from bob.measure.script.compute_perf import main
    cmdline = '--devel=%s --test=%s --self-test' % (DEV_SCORES, TEST_SCORES)
    self.assertEqual(main(cmdline.split()), 0)

  def test02_eval_threshold(self):

    # sanity checks
    self.assertTrue(os.path.exists(DEV_SCORES))

    from bob.measure.script.eval_threshold import main
    cmdline = '--scores=%s --self-test' % (DEV_SCORES,)
    self.assertEqual(main(cmdline.split()), 0)

  def test03_apply_threshold(self):

    # sanity checks
    self.assertTrue(os.path.exists(TEST_SCORES))

    from bob.measure.script.apply_threshold import main
    cmdline = '--scores=%s --self-test' % (TEST_SCORES,)
    self.assertEqual(main(cmdline.split()), 0)

  def test04_compute_perf_5col(self):

    # sanity checks
    self.assertTrue(os.path.exists(DEV_SCORES_5COL))
    self.assertTrue(os.path.exists(TEST_SCORES_5COL))

    from bob.measure.script.compute_perf import main
    cmdline = '--devel=%s --test=%s --parser=bob.measure.load.split_five_column --self-test' % (DEV_SCORES_5COL, TEST_SCORES_5COL)
    self.assertEqual(main(cmdline.split()), 0)

  def test05_compute_cmc(self):

    # sanity checks
    self.assertTrue(os.path.exists(SCORES_4COL_CMC))
    self.assertTrue(os.path.exists(SCORES_5COL_CMC))

    from bob.measure.script.plot_cmc import main
    self.assertEqual(main(['--self-test', '--score-file', SCORES_4COL_CMC, '--log-x-scale']), 0)
    self.assertEqual(main(['--self-test', '--score-file', SCORES_5COL_CMC, '--parser', '5column']), 0)

