#!/usr/bin/env python3
"""
Sparse Matrix Implementation for Data Structures and Algorithms

This script implements a SparseMatrix class that supports:
- Reading a sparse matrix from a file
- Accessing and updating elements
- Adding, subtracting, and multiplying sparse matrices

Input file format:
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)

Invalid formats (e.g., extra whitespace, incorrect parentheses, or non-integer values) raise a ValueError with "Invalid file format".
"""

import sys

class SparseMatrix:
    def __init__(self, num_rows, num_cols):
        """
        Initialize an empty sparse matrix of size num_rows x num_cols.
        Non-zero elements are stored in a dictionary.
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = {}

    @classmethod
    def from_file(cls, file_path):
        """
        Create a SparseMatrix from a file. Raises ValueError for invalid formats.
        """
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except Exception as e:
            raise Exception(f"Failed to open file {file_path}: {e}")

        # Remove empty lines and strip whitespace
        clean_lines = [line.strip() for line in lines if line.strip()]
        if len(clean_lines) < 2:
            raise ValueError("Invalid file format")

        # Parse rows and cols
        try:
            if not clean_lines[0].startswith("rows="):
                raise ValueError
            num_rows = int(clean_lines[0].split("=")[1])

            if not clean_lines[1].startswith("cols="):
                raise ValueError
            num_cols = int(clean_lines[1].split("=")[1])
        except:
            raise ValueError("Invalid file format")

        # Initialize matrix
        matrix = cls(num_rows, num_cols)

        # Parse non-zero elements
        for line in clean_lines[2:]:
            if not (line.startswith("(") and line.endswith(")")):
                raise ValueError("Invalid file format")
            content = line[1:-1]
            parts = content.split(",")
            if len(parts) != 3:
                raise ValueError("Invalid file format")
            try:
                row = int(parts[0].strip())
                col = int(parts[1].strip())
                value = int(parts[2].strip())
            except:
                raise ValueError("Invalid file format")

            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                raise ValueError("Invalid file format")

            matrix.set_element(row, col, value)
        return matrix

    def get_element(self, row, col):
        """Return the element at (row, col), defaulting to 0 if not set."""
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        """Set the element at (row, col) to value."""
        if row < 0 or row >= self.num_rows or col < 0 or col >= self.num_cols:
            raise IndexError("Index out of bounds")
        if value == 0:
            self.elements.pop((row, col), None)
        else:
            self.elements[(row, col)] = value

    def add(self, other):
        """Return a new SparseMatrix representing the sum of self and other."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions")
        result = SparseMatrix(self.num_rows, self.num_cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) + value)
        return result

    def subtract(self, other):
        """Return a new SparseMatrix representing the difference of self and other."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions")
        result = SparseMatrix(self.num_rows, self.num_cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) - value)
        return result

    def multiply(self, other):
        """Return a new SparseMatrix representing the product of self and other."""
        if self.num_cols != other.num_rows:
            raise ValueError("self.num_cols must equal other.num_rows for multiplication")
        result = SparseMatrix(self.num_rows, other.num_cols)

        other_row_map = {}
        for (row, col), value in other.elements.items():
            if row not in other_row_map:
                other_row_map[row] = []
            other_row_map[row].append((col, value))

        for (i, k), self_val in self.elements.items():
            if k in other_row_map:
                for (j, other_val) in other_row_map[k]:
                    current_val = result.get_element(i, j)
                    result.set_element(i, j, current_val + self_val * other_val)
        return result

    def __str__(self):
        """Return a string representation in the input file format, sorted by column index then row index."""
        lines = [f"rows={self.num_rows}", f"cols={self.num_cols}"]
        # Sort by column (key[1]) first, then row (key[0])
        for key in sorted(self.elements.keys(), key=lambda k: (k[1], k[0])):
            value = self.elements[key]
            lines.append(f"({key[0]}, {key[1]}, {value})")
        return "\n".join(lines)

def main():
    """
    Main function to interact with the user, select matrix files by number, choose an operation,
    and optionally save the result.
    """
    print("Sparse Matrix Calculator")
    print("-----------------------")
    print("Available Operations:")
    print("1. Add two matrices")
    print("2. Subtract two matrices")
    print("3. Multiply two matrices")
    choice = input("Choose an operation (1, 2, or 3): ").strip()

    if choice not in ('1', '2', '3'):
        print("Error: Please select 1, 2, or 3.")
        sys.exit(1)

    print("\nSelect matrix files:")
    file1 = input("Enter 1 to specify the first matrix file path: ").strip()
    if file1 != '1':
        print("Error: Please enter '1' to specify the first file.")
        sys.exit(1)
    file1_path = input("Enter the path for the first matrix file: ").strip()

    file2 = input("Enter 2 to specify the second matrix file path: ").strip()
    if file2 != '2':
        print("Error: Please enter '2' to specify the second file.")
        sys.exit(1)
    file2_path = input("Enter the path for the second matrix file: ").strip()

    try:
        matrix1 = SparseMatrix.from_file(file1_path)
        matrix2 = SparseMatrix.from_file(file2_path)
    except Exception as e:
        print(f"Error loading matrices: {e}")
        sys.exit(1)

    try:
        if choice == '1':
            result = matrix1.add(matrix2)
            op_name = "Addition"
        elif choice == '2':
            result = matrix1.subtract(matrix2)
            op_name = "Subtraction"
        else:
            result = matrix1.multiply(matrix2)
            op_name = "Multiplication"
    except Exception as e:
        print(f"Error during {op_name.lower()}: {e}")
        sys.exit(1)

    print(f"\n{op_name} completed successfully.")
    save = input("Would you like to save the result? (y/n): ").strip().lower()
    if save == 'y':
        output_path = input("Enter the output file path: ").strip()
        try:
            with open(output_path, 'w') as f:
                f.write(str(result))
            print(f"Result saved to {output_path}")
        except Exception as e:
            print(f"Error saving result: {e}")
    else:
        print("\nResult:")
        print(result)

if __name__ == "__main__":
    main()