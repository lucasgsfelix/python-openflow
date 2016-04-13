import unittest
import sys
import os

from ofp.v0x01.common import action
from ofp.v0x01.foundation import basic_types


class TestActionHeader(unittest.TestCase):

    def test_get_size(self):
        action_header = action.ActionHeader(1, 40, [15, 15, 15, 15])
        self.assertEqual(action_header.get_size(), 8)

    def test_pack(self):
        action_header = action.ActionHeader(1, 40, [15, 15, 15, 15])
        action_header.pack()

    def test_unpack(self):
        pass


class TestActionOutput(unittest.TestCase):

    def test_get_size(self):
        action_output = action.ActionOutput(0, 8, 8080, 64)
        self.assertEqual(action_output.get_size(), 8)

    def test_pack(self):
        action_output = action.ActionOutput(0, 8, 8080, 64)
        action_output.pack()

    def test_unpack(self):
        pass


class TestActionEnqueue(unittest.TestCase):

    def test_get_size(self):
        action_enqueue = action.ActionEnqueue(11, 16, 80, [1, 2, 3, 4, 5, 6], 1)
        self.assertEqual(action_enqueue.get_size(), 16)

    def test_pack(self):
        action_enqueue = action.ActionEnqueue(11, 16, 80, [1, 2, 3, 4, 5, 6], 1)
        action_enqueue.pack()

    def test_unpack(self):
        pass


class TestActionVlanVid(unittest.TestCase):

    def test_get_size(self):
        action_vlan_vid = action.ActionVlanVid(1, 8, 1, [20, 20])
        self.assertEqual(action_vlan_vid.get_size(), 8)

    def test_pack(self):
        action_vlan_vid = action.ActionVlanVid(1, 8, 1, [20, 20])
        action_vlan_vid.pack()

    def test_unpack(self):
        pass


class TestActionVlanPCP(unittest.TestCase):

    def test_get_size(self):
        action_vlan_pcp = action.ActionVlanPCP(2, 8, 1, [10, 10, 10])
        self.assertEqual(action_vlan_pcp.get_size(), 8)

    def test_pack(self):
        action_vlan_pcp = action.ActionVlanPCP(2, 8, 1, [10, 10, 10])
        action_vlan_pcp.pack()

    def test_unpack(self):
        pass


class TestActionDLAddr(unittest.TestCase):

    def test_get_size(self):
        action_dl_addr = action.ActionDLAddr(
            4, 16, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
        self.assertEqual(action_dl_addr.get_size(), 16)

    def test_pack(self):
        action_dl_addr = action.ActionDLAddr(
            4, 16, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
        action_dl_addr.pack()

    def test_unpack(self):
        pass


class TestActionNWAddr(unittest.TestCase):

    def test_get_size(self):
        action_nw_addr = action.ActionNWAddr(6, 8, 200111222)
        self.assertEqual(action_nw_addr.get_size(), 8)

    def test_pack(self):
        action_nw_addr = action.ActionNWAddr(6, 8, 200111222)
        action_nw_addr.pack()

    def test_unpack(self):
        pass


class TestActionNWTos(unittest.TestCase):

    def test_get_size(self):
        action_nw_tos = action.ActionNWTos(
            7, 8, 10, [0, 10, 10])
        self.assertEqual(action_nw_tos.get_size(), 8)

    def test_pack(self):
        action_nw_tos = action.ActionNWTos(
            7, 8, 10, [0, 10, 10])
        action_nw_tos.pack()

    def test_unpack(self):
        pass


class TestActionTPPort(unittest.TestCase):

    def test_get_size(self):
        action_tp_port = action.ActionTPPort(
            9, 8, 8080, [0, 0])
        self.assertEqual(action_tp_port.get_size(), 8)

    def test_pack(self):
        action_tp_port = action.ActionTPPort(
            9, 8, 8080, [12, 12])
        action_tp_port.pack()

    def test_unpack(self):
        pass


class TestActionVendorHeader(unittest.TestCase):

    def test_get_size(self):
        action_vendor_header = action.ActionVendorHeader(0xffff, 16, 16)
        self.assertEqual(action_vendor_header.get_size(), 8)

    def test_pack(self):
        action_vendor_header = action.ActionVendorHeader(0xffff, 16, 16)
        action_vendor_header.pack()

    def test_unpack(self):
        pass
