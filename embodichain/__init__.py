# ----------------------------------------------------------------------------
# Copyright (c) 2021-2026 DexForce Technology Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import ctypes
import os
import sys
import sysconfig
from pathlib import Path

embodichain_dir = os.path.dirname(__file__)


def _preload_python_shared_library():
    """Preload the active interpreter's shared library for native extensions.

    Some binary dependencies (such as DexSim in uv-managed Python envs) expect
    `libpythonX.Y.so` to already be globally visible at import time.
    """
    if sys.platform != "linux":
        return

    libdir = sysconfig.get_config_var("LIBDIR")
    ldlibrary = sysconfig.get_config_var("LDLIBRARY")
    if not libdir or not ldlibrary:
        return

    libpython = Path(libdir) / ldlibrary
    if not libpython.is_file():
        return

    try:
        ctypes.CDLL(str(libpython), mode=getattr(ctypes, "RTLD_GLOBAL", 0))
    except OSError:
        # Fall back to the system loader if the shared library is already visible
        # or this interpreter was built without a loadable libpython target.
        pass


_preload_python_shared_library()


# Read version from VERSION file
def _get_version():
    version_file = os.path.join(embodichain_dir, "VERSION")
    try:
        with open(version_file, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("VERSION file not found.")
        return "unknown"


__version__ = _get_version()
