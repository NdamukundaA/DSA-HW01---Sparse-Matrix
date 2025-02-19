#include <iostream>
#include <vector>
#include <unordered_map>

class SparseMatrix {
private:
    struct Element {
        int row;
        int col;
        int value;
        Element(int r, int c, int v) : row(r), col(c), value(v) {}
    };
    
    std::vector<Element> elements;
    int rows;
    int cols;
    
public:
    SparseMatrix(int r, int c) : rows(r), cols(c) {}
    
    void insert(int row, int col, int value) {
        if (row >= rows || col >= cols || row < 0 || col < 0) {
            throw std::out_of_range("Invalid matrix position");
        }
        if (value != 0) {
            elements.push_back(Element(row, col, value));
        }
    }
    
    int get(int row, int col) const {
        for (const auto& elem : elements) {
            if (elem.row == row && elem.col == col) {
                return elem.value;
            }
        }
        return 0;
    }
    
    SparseMatrix add(const SparseMatrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions must match for addition");
        }
        
        SparseMatrix result(rows, cols);
        std::unordered_map<int, int> sumMap;
        
        // Add elements from first matrix
        for (const auto& elem : elements) {
            int key = elem.row * cols + elem.col;
            sumMap[key] = elem.value;
        }
        
        // Add elements from second matrix
        for (const auto& elem : other.elements) {
            int key = elem.row * cols + elem.col;
            sumMap[key] += elem.value;
        }
        
        // Create result matrix
        for (const auto& pair : sumMap) {
            if (pair.second != 0) {
                int row = pair.first / cols;
                int col = pair.first % cols;
                result.insert(row, col, pair.second);
            }
        }
        
        return result;
    }
    
    SparseMatrix multiply(const SparseMatrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Invalid matrix dimensions for multiplication");
        }
        
        SparseMatrix result(rows, other.cols);
        
        for (const auto& elem1 : elements) {
            for (const auto& elem2 : other.elements) {
                if (elem1.col == elem2.row) {
                    int newValue = result.get(elem1.row, elem2.col) + 
                                  elem1.value * elem2.value;
                    if (newValue != 0) {
                        result.insert(elem1.row, elem2.col, newValue);
                    }
                }
            }
        }
        
        return result;
    }
    
    SparseMatrix transpose() const {
        SparseMatrix result(cols, rows);
        
        for (const auto& elem : elements) {
            result.insert(elem.col, elem.row, elem.value);
        }
        
        return result;
    }
    
    void print() const {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                std::cout << get(i, j) << " ";
            }
            std::cout << "\n";
        }
    }
};