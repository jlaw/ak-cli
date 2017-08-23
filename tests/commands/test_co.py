"""Tests for our `ak co` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class Testco(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['ak', 'co'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_co_world(self):
        output = popen(['ak', 'co'], stdout=PIPE).communicate()[0]
        self.assertTrue('co!' in output)
