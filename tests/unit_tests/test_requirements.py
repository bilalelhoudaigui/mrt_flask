"""Test availability of required packages."""

import distutils
from distutils import text_file
import unittest
from pathlib import Path

import pkg_resources

_REQUIREMENTS_PATH = Path(__file__).resolve().parents[1].with_name("requirements.txt")


class TestRequirements(unittest.TestCase):
    """Test availability of required packages."""

    def test_requirements(self):
        """Test that each required package is available."""
        # Ref: https://stackoverflow.com/a/45474387/
        requirements = text_file.TextFile(filename=str(_REQUIREMENTS_PATH)).readlines()
        for requirement in requirements:
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)
