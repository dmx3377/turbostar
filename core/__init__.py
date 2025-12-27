# turbostar/core/__init__.py

from .dispatcher import Dispatcher
from .logger import Logger

# This controls what happens when someone types: from turbostar.core import *
__all__ = ["Dispatcher", "Logger"]