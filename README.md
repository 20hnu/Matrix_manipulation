# Matrix Manipulation and Fraction Operations

This repository contains Python implementations for matrix manipulations and fraction operations. The repository includes two Python modules:

## Files
- **`main.py`**: Implements a `Matrix` class for basic matrix operations.
- **`fraction.py`**: Implements a `Fraction` class for basic fraction arithmetic.

## Features

### Matrix Operations (`main.py`)
- **Addition (`+`)**: Adds two matrices of the same dimension.
- **Subtraction (`-`)**: Subtracts one matrix from another.
- **Multiplication (`*`)**: Performs matrix multiplication if dimensions match.
- **Transpose (`transpose()`)**: Returns the transpose of a matrix.
- **Determinant (`determinant()`)**: Returns the determinant of any square matrix

#### Example Usage
```python
from main import Matrix

A = Matrix([[1, 2, 3], [5, 4, 8]])
B = Matrix([[5, 6], [7, 8], [4, 0]])

print(A * B)  # Matrix multiplication example
```

### Fraction Operations (`fraction.py`)
- **Addition (`+`)**: Adds two fractions.
- **Subtraction (`-`)**: Subtracts one fraction from another.
- **Multiplication (`*`)**: Multiplies two fractions.
- **Division (`/`)**: Divides one fraction by another.

#### Example Usage
```python
from fraction import Fraction

f = Fraction(1, 2)
g = Fraction(3, 4)

print(f + g)  # Fraction addition
print(f - g)  # Fraction subtraction
print(f * g)  # Fraction multiplication
print(f / g)  # Fraction division
```

## Installation
### Clone the repository:
```bash
git clone https://github.com/20hnu/matrix_manipulation.git
```
### Navigate into the repository:
```bash
cd matrix_manipulation
```


