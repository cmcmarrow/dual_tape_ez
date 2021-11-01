"""
Copyright 2021 Charles McMarrow
"""

import unittest
# built-in
from typing import List, Optional, Tuple, Union

# dual_tape_ez
from dual_tape_ez.dual_tape_ez import dual_tape_ez_api
from dual_tape_ez.vm import VMState
from .test_files import get_path


def _runner(file: str,
            inputs: Optional[Union[Tuple[str, ...], List[str]]] = None,
            timeout: int = 1000) -> VMState:
    """
    info: Runs VM.
    :param file: str
    :param inputs: Optional[Union[Tuple[str, ...], List[str]]]
    :return: VMState
    """
    if inputs is None:
        inputs = ()
    vm = iter(dual_tape_ez_api(get_path(file), inputs=inputs, sys_output=False, catch_output=True))
    vm_state = next(vm)
    for at, _ in enumerate(vm):
        assert at != timeout
    return vm_state


class VMTests(unittest.TestCase):
    def test_nop(self):
        vm = _runner("nop.dte")
        self.assertEqual(vm.pc, 5)

    def test_halt(self):
        vm = _runner("halt.dte")
        self.assertEqual(vm.pc, 1)

    def test_read(self):
        vm = _runner("read.dte")
        self.assertEqual(vm.output_stream, ["66", "B"])

    def test_read_dynamic(self):
        vm = _runner("read_dynamic.dte")
        self.assertEqual(vm.output_stream, ["67", "C"])

    def test_read_dynamic_instruction(self):
        vm = _runner("read_dynamic_instruction.dte")
        self.assertEqual(vm.output_stream, ["100", "d"])

    def test_add(self):
        vm = _runner("add.dte")
        self.assertEqual(vm.output_stream, ["100", "-60"])

    def test_sub(self):
        vm = _runner("sub.dte")
        self.assertEqual(vm.output_stream, ["-50", "62"])

    def test_write(self):
        vm = _runner("write.dte")
        self.assertEqual(vm.output_stream, ["66", "B"])

    def test_write_dynamic(self):
        vm = _runner("write_dynamic.dte")
        self.assertEqual(vm.output_stream, ["67", "C"])

    def test_write_dynamic_instruction(self):
        vm = _runner("write_dynamic_instruction.dte")
        self.assertEqual(vm.pc, 4)

    def test_jump(self):
        vm = _runner("jump.dte")
        self.assertEqual(vm.pc, 12)

    def test_jump_dynamic(self):
        vm = _runner("jump_dynamic.dte")
        self.assertEqual(vm.pc, 1)

    def test_jump_zero(self):
        vm = _runner("jump_zero.dte")
        self.assertEqual(vm.pc, 1)

    def test_jump_greater(self):
        vm = _runner("jump_greater.dte")
        self.assertEqual(vm.pc, 1)

    def test_in_number(self):
        vm = _runner("in_number.dte", ["101", "66"])
        self.assertEqual(vm.output_stream, ["101", "e", "66", "B"])

    def test_in_character(self):
        vm = _runner("in_character.dte", ["!", "@"])
        self.assertEqual(vm.output_stream, ["33", "!", "64", "@"])
