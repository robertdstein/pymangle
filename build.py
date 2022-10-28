import glob
import numpy as np

from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "pymangle._mangle",
        [
            "pymangle/_mangle.c",
            "pymangle/mangle.c",
            "pymangle/cap.c",
            "pymangle/polygon.c",
            "pymangle/pixel.c",
            "pymangle/point.c",
            "pymangle/stack.c",
            "pymangle/rand.c"
        ],
        include_dirs=[np.get_include()]
    ),
]


class BuildFailed(Exception):
    pass


class ExtBuilder(build_ext):

    def run(self):
        try:
            build_ext.run(self)
        except FileNotFoundError:
            raise BuildFailed('File not found. Could not compile C extension.')

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except ValueError:
            raise BuildFailed('Could not compile C extension.')


def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    setup_kwargs.update(
        {"ext_modules": ext_modules, "cmdclass": {"build_ext": ExtBuilder}}
    )



