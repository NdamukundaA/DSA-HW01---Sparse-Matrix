#include <iostream>
#include "sparse_matrix.cpp"

int main() {
    // Create two sparse matrices
    SparseMatrix m1(3, 3);
    m1.insert(0, 0, 1);
    m1.insert(1, 1, 2);
    m1.insert(2, 2, 3);

    SparseMatrix m2(3, 3);
    m2.insert(0, 0, 4);
    m2.insert(1, 1, 5);
    m2.insert(2, 2, 6);

    std::cout << "Matrix 1:\n";
    m1.print();

    std::cout << "\nMatrix 2:\n";
    m2.print();

    // Test addition
    std::cout << "\nMatrix 1 + Matrix 2:\n";
    SparseMatrix sum = m1.add(m2);
    sum.print();

    // Test multiplication
    std::cout << "\nMatrix 1 * Matrix 2:\n";
    SparseMatrix product = m1.multiply(m2);
    product.print();

    // Test transpose
    std::cout << "\nMatrix 1 Transpose:\n";
    SparseMatrix transpose = m1.transpose();
    transpose.print();

    return 0;
}