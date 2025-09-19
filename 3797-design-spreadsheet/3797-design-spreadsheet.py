class Spreadsheet:
    def __init__(self, rows: int):
        # 26 columns (A-Z), rows given by input
        self.rows = rows
        self.cols = 26
        # Store cell values in a dictionary { "A1": value }
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        # Simply update the dictionary
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        # Reset to 0 (same as removing)
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # formula always of form "=X+Y"
        # remove leading '='
        formula = formula[1:]
        x, y = formula.split('+')

        return self._getOperandValue(x) + self._getOperandValue(y)

    def _getOperandValue(self, operand: str) -> int:
        # If operand is a number
        if operand.isdigit():
            return int(operand)
        # Else, it is a cell reference like "A1"
        return self.cells.get(operand, 0)


# Example usage:
spreadsheet = Spreadsheet(3)
print(spreadsheet.getValue("=5+7"))   # 12
spreadsheet.setCell("A1", 10)
print(spreadsheet.getValue("=A1+6"))  # 16
spreadsheet.setCell("B2", 15)
print(spreadsheet.getValue("=A1+B2")) # 25
spreadsheet.resetCell("A1")
print(spreadsheet.getValue("=A1+B2")) # 15
