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
    pass
