from typing import List, Any, Tuple, Union, Generator


class MatrixManipulation:
    def __init__(self, matrix: List[List[Any]]) -> None:
        """
        Initialize the MatrixManipulation object.

        Args:
            matrix (List[List[Any]]): A 2D list representing the matrix.
        """
        self.matrix = matrix

    def __getitem__(self, idx: int) -> List[Any]:
        """
        Retrieve a specific row of the matrix.

        Args:
            idx (int): Row index.

        Returns:
            List[Any]: The row at the specified index.
        """
        return self.matrix[idx]

    def __setitem__(self, idx: int, value: List[Any]) -> None:
        """
        Set a specific row of the matrix.

        Args:
            idx (int): Row index.
            value (List[Any]): New row to replace the existing one.
        """
        self.matrix[idx] = value

    def __iter__(self):
        """
        Enable iteration over rows of the matrix.

        Returns:
            Iterator: An iterator over the rows.
        """
        return iter(self.matrix)

    def get_primary_diagnonals(self) -> List[List[Union[Any, str]]]:
        """
        Retrieves the primary diagonals from the matrix (top-left -> bottom right).

        Returns:
            List[List[Union[Any, str]]]: A list of primary diagonals.
        """
        rows, cols = len(self.matrix), len(self.matrix[0])
        diagonals = []
        for d in range(-(rows - 1), cols):
            diagonal = []
            for r in range(rows):
                c = r - d
                if 0 <= c < cols:
                    value = self.matrix[r][c]
                    diagonal.append(value)
            if len(diagonal) and isinstance(diagonal[0], str):
                diagonal = ''.join(diagonal)
            diagonals.append(diagonal)
        return diagonals

    def get_secondary_diagnonals(self) -> List[List[Union[Any, str]]]:
        """
        Retrieves the secondary diagonals from the matrix (top-right -> bottom-left).

        Returns:
            List[List[Union[Any, str]]]: A list of secondary diagonals.
        """
        rows, cols = len(self.matrix), len(self.matrix[0])
        diagonals = []
        for d in range(rows + cols - 1):
            diagonal = []
            for r in range(rows):
                c = d - r
                if 0 <= c < cols:
                    value = self.matrix[r][c]
                    diagonal.append(value)
            if len(diagonal) and isinstance(diagonal[0], str):
                diagonal = ''.join(diagonal)
            diagonals.append(diagonal)
        return diagonals

    def get_diagonals(self) -> List[List[Union[Any, str]]]:
        """
        Retrieve all primary and secondary diagonals from the matrix.

        Returns:
            List[List[Union[Any, str]]]: A list of all diagonals.
        """
        diagonals = []
        diagonals.extend(self.get_primary_diagnonals())
        diagonals.extend(self.get_secondary_diagnonals())
        return diagonals

    def shape(self) -> Tuple[int, int]:
        """
        Get the dimensions of the matrix.

        Returns:
            Tuple[int, int]: A tuple representing the shape (rows, columns).
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0]) if rows > 0 else 0
        return rows, cols

    def get_row(self, row_idx: int) -> List[Any]:
        """
        Retrieve a specific row from the matrix.

        Args:
            row_idx (int): The row index to retrieve.

        Returns:
            List[Any]: The row at the specified index.
        """
        return self.matrix[row_idx]

    def get_column(self, col_idx: int) -> List[Any]:
        """
        Retrieve a specific column from the matrix.

        Args:
            col_idx (int): The column index to retrieve.

        Returns:
            List[Any]: The column at the specified index.
        """
        return [row[col_idx] for row in self.matrix]

    def add_row(self, new_row: List[Any]) -> None:
        """
        Add a new row to the matrix.

        Args:
            new_row (List[Any]): The row to add.

        Raises:
            ValueError: If the new row length does not match the matrix column count.
        """
        if len(new_row) != len(self.matrix[0]):
            raise ValueError("New row must have the same number of columns as the matrix.")
        self.matrix.append(new_row)

    def add_column(self, new_column: List[Any]) -> None:
        """
        Add a new column to the matrix.

        Args:
            new_column (List[Any]): The column to add.

        Raises:
            ValueError: If the new column length does not match the matrix row count.
        """
        if len(new_column) != len(self.matrix):
            raise ValueError("New column must have the same number of rows as the matrix.")
        for i, val in enumerate(new_column):
            self.matrix[i].append(val)

    def remove_row(self, row_idx: int) -> None:
        """
        Remove a row from the matrix.

        Args:
            row_idx (int): The index of the row to remove.
        """
        del self.matrix[row_idx]

    def remove_column(self, col_idx: int) -> None:
        """
        Remove a column from the matrix.

        Args:
            col_idx (int): The index of the column to remove.
        """
        for row in self.matrix:
            del row[col_idx]

    def flatten(self) -> List[Any]:
        """
        Flatten the matrix into a single list.

        Returns:
            List[Any]: The flattened matrix as a list.
        """
        return [elem for row in self.matrix for elem in row]

    def scalar_multiply(self, scalar: Union[int, float]) -> List[List[Union[int, float]]]:
        """
        Multiply every element in the matrix by a scalar.

        Args:
            scalar (Union[int, float]): The scalar value to multiply by.

        Returns:
            List[List[Union[int, float]]]: A new matrix with scaled elements.
        """
        return [[elem * scalar for elem in row] for row in self.matrix]

    def elementwise_add(self, other: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
        """
        Perform element-wise addition with another matrix.

        Args:
            other (List[List[Union[int, float]]]): The other matrix to add.

        Returns:
            List[List[Union[int, float]]]: The resulting matrix.

        Raises:
            ValueError: If the matrices do not have the same dimensions.
        """
        if self.shape() != MatrixManipulation(other).shape():
            raise ValueError("Matrices must have the same shape for element-wise addition.")
        return [[self.matrix[i][j] + other[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]

    def transpose(self) -> List[List[Any]]:
        """
        Transpose the matrix (swap rows and columns).

        Returns:
            List[List[Any]]: The transposed matrix.
        """
        return [list(row) for row in zip(*self.matrix)]

    def rotate_90_clockwise(self) -> List[List[Any]]:
        """
        Rotate the matrix 90 degrees clockwise.

        Returns:
            List[List[Any]]: The rotated matrix.
        """
        return [list(row) for row in zip(*self.matrix[::-1])]

    def get_rows(self) -> List[List[Any]]:
        """
        Get all rows of the matrix as a 2D list.

        Returns:
            List[List[Any]]: A 2D list containing all rows.
        """
        return self.matrix

    def get_cols(self) -> List[List[Union[Any, str]]]:
        """
        Get all columns of the matrix.

        Returns:
            List[List[Union[Any, str]]]: A 2D list containing all columns.
        """
        cols = []
        for col_idx in range(len(self.matrix[0])):
            column = []
            for row in self.matrix:
                value = row[col_idx]
                column.append(value)
            if len(column) and isinstance(column[0], str):
                column = ''.join(column)
            cols.append(column)
        return cols

    def print_matrix(self) -> None:
        """
        Print the matrix in a readable format.
        """
        for row in self.matrix:
            print(row)
