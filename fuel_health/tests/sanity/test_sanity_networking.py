# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
from nose.plugins.attrib import attr
from nose.tools import timed

from fuel_health import nmanager

LOG = logging.getLogger(__name__)


class NetworksTest(nmanager.SanityChecksTest):
    """
    TestClass contains tests check base networking functionality
    """

    @attr(type=['sanity', 'fuel'])
    @timed(6)
    def test_list_networks(self):
        """Networks availability
        Test checks that available networks can be listed.
        Target component: Nova Networking.

        Scenario:
            1. Request list of networks.
            2. Check response.
        Duration: 1-6 s.
        """
        fail_msg = ("Network list is unavailable. "
                    "Looks like something is broken in Network Networking")
        try:
            networks = self._list_networks(self.compute_client)
        except Exception as exc:
            LOG.debug(exc)
            self.fail(fail_msg)

        self.verify_response_true(len(networks) >= 0,
                                  'Step 2 failed:' + fail_msg)

    @attr(type=['sanity', 'fuel'])
    @timed(6)
    def test_list_ports(self):
        """Ports availability
        Test checks that existing ports can be listed.
        Target component: Nova Networking.

        Scenario:
            1. Request list of ports.
            2. Check response.
        Duration: 1-6 s.
        """
        fail_msg = ('Ports list is unavailable. '
                    'Looks like something is broken in Network '
                    '(Neutron or Nova).')
        try:
            ports = self._list_ports(self.compute_client)
        except Exception as exc:
            LOG.debug(exc)
            self.fail('Step 1 failed: ' + fail_msg)
        self.verify_response_true(len(ports) >= 0, 'Step 2 failed:' + fail_msg)