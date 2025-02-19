const { SparseMatrix } = require('./sparse_matrix');

// Create two sparse matrices
const m1 = new SparseMatrix(3, 3);
m1.insert(0, 0, 1);
m1.insert(1, 1, 2);
m1.insert(2, 2, 3);

const m2 = new SparseMatrix(3, 3);
m2.insert(0, 0, 4);
m2.insert(1, 1, 5);
m2.insert(2, 2, 6);

console.log('Matrix 1:');
m1.print();

console.log('\nMatrix 2:');
m2.print();

// Test addition
console.log('\nMatrix 1 + Matrix 2:');
const sum = m1.add(m2);
sum.print();

// Test multiplication
console.log('\nMatrix 1 * Matrix 2:');
const product = m1.multiply(m2);
product.print();

// Test transpose
console.log('\nMatrix 1 Transpose:');
const transpose = m1.transpose();
transpose.print();