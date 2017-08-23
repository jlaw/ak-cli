"""The co command."""


from json import dumps

from .base import Base


class Co(Base):
    def run(self):
        print('co!')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
