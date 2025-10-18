import numpy as np

def gaussian_elimination(A, b):
    Ab = np.hstack((A, b.reshape(-1,1)))
    
    return np.linalg.solve(A, b)

if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 11])
    x = np.linalg.solve(A, b)
    print(f"Solution: {x}")