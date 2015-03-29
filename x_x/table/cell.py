from __future__ import unicode_literals
from six import PY3, integer_types

if PY3:
    unicode = str


class Cell(object):

    def __init__(self, value):
        self.original_value = value

        self.coordinates = (0, 0)

        self._divine_type()

    def _divine_type(self):

        self.type = str

        if self.original_value == "0" or not self.original_value.startswith("0"):

            for t in integer_types:
                try:
                    t(self.original_value)
                    self.type = t
                    break
                except:
                    pass

            if self.type == str:

                try:
                    float(self.original_value)
                    self.type = float
                except:
                    pass

        if not PY3:
            self.value = unicode(self.original_value, "utf-8", "ignore")
        else:
            self.value = str(self.original_value)
