# 题目1：二阶行列式计算
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

if __name__ == "__main__":
    mat = np.array([[1, 2], [3, 4]])
    res = determinant(mat)
    print(f"行列式结果：{res:.2f}")
