"""
Core module for WinVirtualDesktop
"""

from winvirtualdesktop.core.base_hypervisor import BaseHypervisor, HypervisorType, VMState
from winvirtualdesktop.core.config import VMConfig, OSType, NetworkMode
from winvirtualdesktop.core.vm_manager import VMManager

__all__ = [
    'BaseHypervisor',
    'HypervisorType',
    'VMState',
    'VMConfig',
    'OSType',
    'NetworkMode',
    'VMManager',
]