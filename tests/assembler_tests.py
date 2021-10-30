"""
Copyright 2021 Charles McMarrow
"""

# built-in
import unittest

# dual_tape_ez
from dual_tape_ez.assembler import assembler, AssemblerError
from .test_files import get_path


class AssemblerTests(unittest.TestCase):
    def test_minimum(self):
        entry_point, instructions, data = assembler(get_path("minimum.dte"))
        self.assertEqual(entry_point, 0)
        self.assertIsInstance(instructions, dict)
        self.assertIsInstance(data, dict)

    def test_full_load(self):
        entry_point, instructions, data = assembler(get_path("full_load.dte"))
        self.assertEqual(entry_point, 7)

        for spot, i in enumerate("nxnnxnxnnnxnxnnxx"):
            self.assertEqual(instructions[spot], ord(i))

        self.assertNotIn(0, data)
        self.assertEqual(data[1], -444)
        self.assertEqual(data[2], 6)
        self.assertEqual(data[3], 0)
        self.assertNotIn(4, data)
        self.assertEqual(data[5], 5)
        self.assertNotIn(6, data)
        self.assertEqual(data[7], 666)
        self.assertEqual(data[8], 35)
        self.assertEqual(data[9], 64)
        self.assertEqual(data[10], 65)
        self.assertEqual(data[11], 345)
        self.assertEqual(data[12], 1)
        self.assertNotIn(13, data)
        self.assertNotIn(14, data)
        self.assertEqual(data[15], 13)
        self.assertEqual(data[16], -27986354294658737869245376892435768254387962453)

    def test_missing_name(self):
        self.assertRaises(AssemblerError, assembler, get_path("missing_name.dte"))

    def test_name_collection(self):
        self.assertRaises(AssemblerError, assembler, get_path("name_collection.dte"))

    def test_missing_entry_point(self):
        self.assertRaises(AssemblerError, assembler, get_path("missing_entry_point.dte"))

    def test_file_not_found(self):
        self.assertRaises(AssemblerError, assembler, "missing_file_273A450827C9450923857.dte")

    def test_bad_character(self):
        self.assertRaises(AssemblerError, assembler, get_path("bad_character.dte"))

    def test_bad_character_2(self):
        self.assertRaises(AssemblerError, assembler, get_path("bad_character_2.dte"))

    def test_bad_data(self):
        self.assertRaises(AssemblerError, assembler, get_path("bad_data.dte"))

    def test_bad_instruction(self):
        self.assertRaises(AssemblerError, assembler, get_path("bad_instruction.dte"))
