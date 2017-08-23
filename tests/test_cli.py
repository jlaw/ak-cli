"""Tests for our main ak CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from ak import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['ak', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['ak', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['ak', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
