class SparseMatrix {
    constructor(rows, cols) {
        this.rows = rows;
        this.cols = cols;
        this.elements = [];
    }

    insert(row, col, value) {
        if (row >= this.rows || col >= this.cols || row < 0 || col < 0) {
            throw new Error("Invalid matrix position");
        }
        if (value !== 0) {
            this.elements.push({ row, col, value });
        }
    }

    get(row, col) {
        for (const elem of this.elements) {
            if (elem.row === row && elem.col === col) {
                return elem.value;
            }
        }
        return 0;
    }

    add(other) {
        if (this.rows !== other.rows || this.cols !== other.cols) {
            throw new Error("Matrix dimensions must match for addition");
        }

        const result = new SparseMatrix(this.rows, this.cols);
        const sumMap = new Map();

        // Add elements from first matrix
        for (const elem of this.elements) {
            const key = elem.row * this.cols + elem.col;
            sumMap.set(key, elem.value);
        }

        // Add elements from second matrix
        for (const elem of other.elements) {
            const key = elem.row * this.cols + elem.col;
            const currentValue = sumMap.get(key) || 0;
            sumMap.set(key, currentValue + elem.value);
        }

        // Create result matrix
        for (const [key, value] of sumMap) {
            if (value !== 0) {
                const row = Math.floor(key / this.cols);
                const col = key % this.cols;
                result.insert(row, col, value);
            }
        }

        return result;
    }

    multiply(other) {
        if (this.cols !== other.rows) {
            throw new Error("Invalid matrix dimensions for multiplication");
        }

        const result = new SparseMatrix(this.rows, other.cols);

        for (const elem1 of this.elements) {
            for (const elem2 of other.elements) {
                if (elem1.col === elem2.row) {
                    const newValue = result.get(elem1.row, elem2.col) +
                                   elem1.value * elem2.value;
                    if (newValue !== 0) {
                        result.insert(elem1.row, elem2.col, newValue);
                    }
                }
            }
        }

        return result;
    }

    transpose() {
        const result = new SparseMatrix(this.cols, this.rows);

        for (const elem of this.elements) {
            result.insert(elem.col, elem.row, elem.value);
        }

        return result;
    }

    print() {
        for (let i = 0; i < this.rows; i++) {
            let row = [];
            for (let j = 0; j < this.cols; j++) {
                row.push(this.get(i, j));
            }
            console.log(row.join(' '));
        }
    }
}

module.exports = { SparseMatrix };