
import atexit
import sys

# Inspector class decides what packages are hits

class Inspector:

    def __call__(self, sys_modules):
        raise NotImplementedError

class NameInspector(Inspector):
    """Just compare names, but could be much more elaborate"""

    def __init__(self, packages):
        self.packages = packages

    def __call__(self, sys_modules):
        return [m for m in sys_modules if m in self.packages]

# Reporter class does some reporting with the list of hits

class Reporter:

    def __call__(self, hits):
        raise NotImplementedError

import json
import os
from uuid import uuid4

class JSONReporter(Reporter):
    """Put hits in JSON file with horrible name"""

    def __init__(self, dirname):
        self.dirname = dirname

    def __call__(self, hits):
        path = os.path.join(self.dirname, f"{uuid4()}.json")
        with open(path, "w") as stream:
            json.dump(hits, stream)

# Registers the exit hook

def register_exit_hook(inspector, reporter):
    def exit_hook():
        reporter(inspector(sys.modules))
    atexit.register(exit_hook)

register_exit_hook(
    NameInspector(["numpy", "scipy"]),
    JSONReporter("/tmp")
)
