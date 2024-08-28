##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from cba_lib.cba_lib import CbaLib

import unittest


class TestCbaLib(unittest.TestCase):

    def setUp(self):
        self.lib = CbaLib()
