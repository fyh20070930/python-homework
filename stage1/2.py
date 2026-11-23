# 题目2：三阶行列式计算
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

if __name__ == "__main__":
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    res = determinant(mat)
    print(f"行列式结果: {res:.2f}")
