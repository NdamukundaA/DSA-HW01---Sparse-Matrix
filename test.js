const SparseMatrix = require('./dsa/sparse_matrix/code/src/SparseMatrix');

// Test matrix creation and basic operations
function testBasicOperations() {
    console.log('Testing basic matrix operations...');
    
    const matrix = new SparseMatrix();
    matrix.setDimensions(3, 3);
    
    // Set some values
    matrix.set(0, 0, 1);
    matrix.set(1, 1, 2);
    matrix.set(2, 2, 3);
    
    console.log('Original matrix:');
    console.log(matrix.toString());
    
    // Test get operation
    console.log('\nTesting get operation:');
    console.log(`Value at (1,1): ${matrix.get(1, 1)}`);
    console.log(`Value at (0,1): ${matrix.get(0, 1)}`);
}

// Test matrix addition
function testAddition() {
    console.log('\nTesting matrix addition...');
    
    const matrix1 = new SparseMatrix();
    const matrix2 = new SparseMatrix();
    
    matrix1.setDimensions(2, 2);
    matrix2.setDimensions(2, 2);
    
    matrix1.set(0, 0, 1);
    matrix1.set(1, 1, 2);
    
    matrix2.set(0, 0, 2);
    matrix2.set(0, 1, 3);
    
    console.log('Matrix 1:');
    console.log(matrix1.toString());
    
    console.log('\nMatrix 2:');
    console.log(matrix2.toString());
    
    const sum = matrix1.add(matrix2);
    console.log('\nSum:');
    console.log(sum.toString());
}

// Test matrix multiplication
function testMultiplication() {
    console.log('\nTesting matrix multiplication...');
    
    const matrix1 = new SparseMatrix();
    const matrix2 = new SparseMatrix();
    
    matrix1.setDimensions(2, 3);
    matrix2.setDimensions(3, 2);
    
    matrix1.set(0, 0, 1);
    matrix1.set(0, 2, 2);
    matrix1.set(1, 1, 3);
    
    matrix2.set(0, 0, 1);
    matrix2.set(1, 1, 2);
    matrix2.set(2, 1, 3);
    
    console.log('Matrix 1:');
    console.log(matrix1.toString());
    
    console.log('\nMatrix 2:');
    console.log(matrix2.toString());
    
    const product = matrix1.multiply(matrix2);
    console.log('\nProduct:');
    console.log(product.toString());
}

// Test matrix transpose
function testTranspose() {
    console.log('\nTesting matrix transpose...');
    
    const matrix = new SparseMatrix();
    matrix.setDimensions(2, 3);
    
    matrix.set(0, 0, 1);
    matrix.set(0, 2, 2);
    matrix.set(1, 1, 3);
    
    console.log('Original matrix:');
    console.log(matrix.toString());
    
    const transposed = matrix.transpose();
    console.log('\nTransposed matrix:');
    console.log(transposed.toString());
}

// Run all tests
console.log('Starting Sparse Matrix Tests\n');
testBasicOperations();
testAddition();
testMultiplication();
testTranspose();
console.log('\nAll tests completed.');