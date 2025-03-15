class Matrix:

    def __init__(self,data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        return "\n".join(['\t'.join(map(str, row)) for row in self.data])
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimension must match for addition")
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.rows:
            raise ValueError("Matrix dimension must match for addition")
        result = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] - other.data[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimension must match for multiplication")
        result = [[0 for _ in range(self.rows)]  for _ in range(other.cols)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)


    def transpose(self):
        result = [[0 for _ in range(self.rows)]for _ in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                result[i][j] = self.data[j][i]
        return Matrix(result)
    
    def determinant(self):
            if self.rows != self.cols:
                raise ValueError("Matrix should be square to calculate determinant") 
            return self._recursive_determinant(self.data)
            
    def _recursive_determinant(self, matrix):
            if len(matrix) ==1:
                return matrix[0][0]
                
            if len(matrix) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
            det =0
            for c in range(len(matrix)):
                sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
                det += ((-1) ** c) * matrix[0][c] * self._recursive_determinant(sub_matrix)
                
            return det

if __name__ == "__main__":
    A = Matrix([[1,2], [5,4]])
    B = Matrix([[5, 6,3], [7, 8,1],[4,0,7]])
    print(A)
    print(B)
    print(A.transpose())
    print(A.determinant())
    print(B.determinant())