import importlib
import inspect
import os
from glob import glob

from xplainer.backend.tools.abstract_tool import AbstractTool

files = glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.py"))

#
# Export all tools (non abstract implementations of an AbstractTool class) from this module
#

tools = []
for file in files:
    name = os.path.splitext(os.path.basename(file))[0]
    if name == "__init__":
        continue

    module = importlib.import_module(f".{name}", __package__)
    for name, member in inspect.getmembers(module):
        if inspect.isclass(member) and issubclass(member, AbstractTool) and not inspect.isabstract(member):
            tools.append(member)

__all__ = tools
