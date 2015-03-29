from .cell import Cell


class Column(tuple):

    def __init__(self, cells, column_number=0):

        if not all([isinstance(c, Cell) for c in cells]):
            raise ValueError

        tuple.__init__(cells)

        self._column_number = column_number
        self.column_number = column_number

    @classmethod
    def from_values(cls, value_list, **kwargs):

        cells = [Cell(v) for v in value_list]
        return cls(cells, **kwargs)

    @property
    def column_number(self):
        return self._column_number

    @column_number.setter
    def column_number(self, n):
        self._column_number = n
        self._update_coordinates()
        self.width = self._find_width()

    def _update_coordinates(self):
        for i, c in enumerate(self):
            c.coordinates = (i, self.column_number)

    def _find_width(self):
        return max([len(c.value) for c in self])
