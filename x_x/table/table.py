from .column import Column


class Table(tuple):

    def __init__(self, columns, corner="+", vertical="|", horizontal="-"):

        if not all([isinstance(c, Column) for c in columns]):
            raise ValueError

        if len(set([len(c) for c in columns])) != 1:
            raise ValueError("Columns must all have the same length!")

        self.corner = corner
        self.vertical = vertical
        self.horizontal = horizontal
        self.num_rows = len(columns[0])

        tuple.__init__(columns)

    @classmethod
    def from_rows(cls, rows, **kwargs):

        if len(set([len(row) for row in rows])) != 1:
            raise ValueError("Rows must all have the same length!")

        num_cols = len(rows[0])
        col_values = [[] for i in range(num_cols)]

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                col_values[j].append(value)

        columns = [Column.from_values(cv) for cv in col_values]
        return cls(columns, **kwargs)

    def _row_divider(self):
        return self.corner + self.corner.join([self.horizontal * (c.width + 2) for c in self]) + self.corner

    def to_string(self):

        result = ""

        for i in range(self.num_rows):
            result += "{}\n".format(self._row_divider())
            for c in self:
                cell = c[i]
                spaces = " " * (c.width - len(cell.value))
                result += "{} {}{} ".format(self.vertical, cell.value, spaces)
            result += "{}\n".format(self.vertical)

        result += "{}\n".format(self._row_divider())

        return result
